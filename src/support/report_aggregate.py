from collections import defaultdict
from glob import glob
from json import load
from operator import itemgetter
from os.path import abspath, dirname
from typing import Any, DefaultDict, Iterable

from packaging.version import Version
from packaging.version import parse as parseVersion


def make_header(versions: Iterable[Version]) -> str:
    cols = " | ".join(str(v) for v in versions)
    return f"| Command | {cols} |\n" if cols else "| Command |\n"


def make_divider(n_versions: int) -> str:
    return "|" + ":---|" + ("---:|" * n_versions) + "\n"


def fmt_pct(n: float) -> str:
    return f"{n:.2f}%"


def pct_other_vs_ref(other: float, ref: float) -> str:
    # Percent difference of "other" relative to "ref": ((other/ref) - 1) * 100
    if other > 0 and ref > 0:
        return fmt_pct((other / ref - 1.0) * 100.0)
    return "--"


def pct_ref_vs_other(ref: float, other: float) -> str:
    # Percent difference of "ref" relative to "other": ((ref/other) - 1) * 100
    if ref > 0 and other > 0:
        return fmt_pct((ref / other - 1.0) * 100.0)
    return "--"


def val_or_dash(x: float) -> str:
    return str(x) if x and x > 0 else "--"


def main() -> int:
    ROOT_DIR = dirname(abspath(__file__))

    performance: list[dict[str, dict[str, Any]]] = []
    filenames = f"{ROOT_DIR}/../../report/json/*.json"
    for file in sorted(glob(filenames), reverse=True):
        with open(file, encoding="utf-8") as jfile:
            loaded = load(jfile)
            for item in loaded:
                item["version"] = parseVersion(item["version"])
            performance.extend(loaded)

    performance.sort(key=itemgetter("version"), reverse=True)
    performance.sort(key=itemgetter("command"))

    versions_desc: list[Version] = list(sorted({item["version"] for item in performance}, reverse=True))
    print(f"Found {len(versions_desc)} versions: {', '.join(str(v) for v in versions_desc)}")

    commands: DefaultDict[str, dict[Version, dict[str, Any]]] = defaultdict(dict)
    for item in performance:
        commands[item["command"]][item["version"]] = item

    with open(f"{ROOT_DIR}/compare.md", "w", encoding="utf-8") as file_to_save:
        file_to_save.write("### **Comparison**\n")

        # For each reference version, compare against all older versions
        for ref_version in versions_desc:
            older_versions = [v for v in versions_desc if v < ref_version]
            if not older_versions:
                # No older versions to compare
                continue

            # Speed comparison (Mean/Median): "older vs ref"
            file_to_save.write("\n")
            file_to_save.write(f"#### How much faster {ref_version} is? (Mean / Median vs older)\n")
            file_to_save.write(make_header(older_versions))
            file_to_save.write(make_divider(len(older_versions)))

            for command in sorted(commands.keys()):
                cmd_data = commands[command]
                ref_item = cmd_data.get(ref_version)
                ref_mean = ref_item.get("mean", 0) if ref_item else 0
                ref_median = ref_item.get("median", 0) if ref_item else 0

                cells: list[str] = []
                for older in older_versions:
                    older_item = cmd_data.get(older)
                    if older_item and ref_item:
                        mean_c = pct_other_vs_ref(older_item.get("mean", 0), ref_mean)
                        median_c = pct_other_vs_ref(older_item.get("median", 0), ref_median)
                        cells.append(f"{mean_c} / {median_c}")
                    else:
                        cells.append("-- / --")
                file_to_save.write(f"| `{command}` | {' | '.join(cells)} |\n")

            file_to_save.write("---\n")

            # Memory comparison: "ref vs older"
            file_to_save.write("\n")
            file_to_save.write(f"#### How much more memory {ref_version} uses? (vs older)\n")
            file_to_save.write(make_header(older_versions))
            file_to_save.write(make_divider(len(older_versions)))

            for command in sorted(commands.keys()):
                cmd_data = commands[command]
                ref_item = cmd_data.get(ref_version)
                ref_mem = ref_item.get("memory", 0) if ref_item else 0

                cells: list[str] = []
                for older in older_versions:
                    older_item = cmd_data.get(older)
                    if older_item and ref_item:
                        mem_c = pct_ref_vs_other(ref_mem, older_item.get("memory", 0))
                        cells.append(mem_c)
                    else:
                        cells.append("--")
                file_to_save.write(f"| `{command}` | {' | '.join(cells)} |\n")

            file_to_save.write("---\n")

        file_to_save.write("\n")
        file_to_save.write("#### **Execution**\n")

        # Mean
        file_to_save.write("\n")
        file_to_save.write("##### **Mean [s]**\n")
        file_to_save.write(make_header(versions_desc))
        file_to_save.write(make_divider(len(versions_desc)))
        for command in sorted(commands.keys()):
            cmd_data = commands[command]
            cells = [val_or_dash((cmd_data.get(v) or {}).get("mean", -1)) for v in versions_desc]
            file_to_save.write(f"| `{command}` | {' | '.join(cells)} |\n")

        # Median
        file_to_save.write("\n")
        file_to_save.write("##### **Median [s]**\n")
        file_to_save.write(make_header(versions_desc))
        file_to_save.write(make_divider(len(versions_desc)))
        for command in sorted(commands.keys()):
            cmd_data = commands[command]
            cells = [val_or_dash((cmd_data.get(v) or {}).get("median", -1)) for v in versions_desc]
            file_to_save.write(f"| `{command}` | {' | '.join(cells)} |\n")

        # Memory
        file_to_save.write("\n")
        file_to_save.write("#### **Memory Usage**\n")
        file_to_save.write("\n")
        file_to_save.write("##### **MEM [MB]**\n")
        file_to_save.write(make_header(versions_desc))
        file_to_save.write(make_divider(len(versions_desc)))
        for command in sorted(commands.keys()):
            cmd_data = commands[command]
            cells = [val_or_dash((cmd_data.get(v) or {}).get("memory", -1)) for v in versions_desc]
            file_to_save.write(f"| `{command}` | {' | '.join(cells)} |\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
