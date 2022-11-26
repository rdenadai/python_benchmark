from collections import defaultdict
from glob import glob
from json import load
from operator import itemgetter
from os.path import abspath, dirname
from typing import DefaultDict, Dict, List

from packaging.version import parse as parseVersion


def main() -> int:
    DIVISOR = "|:---|---:|---:|---:|---:|---:|---:|\n"
    ROOT_DIR = dirname(abspath(__file__))

    performance = []
    filenames = f"{ROOT_DIR}/../../report/json/*.json"
    for file in sorted(glob(filenames)):
        with open(file, encoding="utf-8") as jfile:
            loaded = load(jfile)
            for item in loaded:
                item["version"] = parseVersion(item["version"])
            performance.extend(loaded)
    performance.sort(key=itemgetter("version", "command"))

    final: DefaultDict[str, List[Dict]] = defaultdict(list)
    for item in performance:
        final[item.get("command")] += [item]

    with open(f"{ROOT_DIR}/compare.md", "w", encoding="utf-8") as file_to_save:
        file_to_save.write("### **Comparison**\n")
        # Mean Compare
        file_to_save.write("\n")
        file_to_save.write("#### How much faster 3.11 is? (Mean / Median from 3.6 to 3.10)\n")
        file_to_save.write("| Command | 3.6 (Mean / Median) | 3.7 (...) | 3.8 (...) | 3.9 (...) | 3.10 (...) |\n")
        file_to_save.write("|:---|---:|---:|---:|---:|---:|\n")
        for command, items in final.items():
            python_latest = items[-1]
            mean, median = python_latest.get("mean"), python_latest.get("median")
            diff_percentage = []
            for item in items[:-1]:
                mean_c, median_c = "--", "--"
                if (x := item.get("mean")) > 0:
                    mean_c = f"{((x * 100 / mean) - 100):.2f}%"
                if (x := item.get("median")) > 0:
                    median_c = f"{((x * 100 / median) - 100):.2f}%"
                diff_percentage.append(f"{mean_c} / {median_c}")
            file_to_save.write(f"| `{command}` | {' | '.join(diff_percentage)} |\n")
        file_to_save.write("---\n")
        # Median Compare
        file_to_save.write("\n")
        file_to_save.write("#### How much more memory 3.11 uses? (Memory from 3.6 to 3.10)\n")
        file_to_save.write("| Command |  3.6 | 3.7 | 3.8 | 3.9 | 3.10 |\n")
        file_to_save.write("|:---|---:|---:|---:|---:|---:|\n")
        for command, items in final.items():
            python_latest = items[-1].get("memory")
            diff_percentage = " | ".join(
                f"{round((python_latest * 100 / x) - 100, 2)}%" if (x := item.get("memory")) > 0 else "--"
                for item in items[:-1]
            )
            file_to_save.write(f"| `{command}` | {diff_percentage} |\n")
        file_to_save.write("---\n")
        # Mean
        file_to_save.write("\n")
        file_to_save.write("#### **Execution**\n")
        file_to_save.write("\n")
        file_to_save.write(
            "| Command |  Mean 3.6 [s] | Mean 3.7 [s] | Mean 3.8 [s] | Mean 3.9 [s] | Mean 3.10 [s] | Mean 3.11 [s] |\n"
        )
        file_to_save.write(DIVISOR)
        for command, items in final.items():
            file_to_save.write(
                f'| `{command}` | {" | ".join(str(x) if (x := item.get("mean", -1)) > 0 else "--" for item in items)} |\n'
            )
        # Median
        file_to_save.write("\n")
        file_to_save.write(
            "| Command |  Median 3.6 [s] | Median 3.7 [s] | Median 3.8 [s] | Median 3.9 [s] | Median 3.10 [s] | Median 3.11 [s] |\n"
        )
        file_to_save.write(DIVISOR)
        for command, items in final.items():
            file_to_save.write(
                f'| `{command}` | {" | ".join(str(x) if (x := item.get("median", -1)) > 0 else "--" for item in items)} |\n'
            )
        # Memory
        file_to_save.write("\n")
        file_to_save.write("#### **Memory Usage**\n")
        file_to_save.write("\n")
        file_to_save.write(
            "| Command |  MEM 3.6 [MB] | MEM 3.7 [MB] | MEM 3.8 [MB] | MEM 3.9 [MB] | MEM 3.10 [MB] | MEM 3.11 [MB] |\n"
        )
        file_to_save.write(DIVISOR)
        for command, items in final.items():
            file_to_save.write(
                f'| `{command}` | {" | ".join(str(x) if (x := item.get("memory", -1)) > 0 else "--" for item in items)} |\n'
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
