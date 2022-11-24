from collections import defaultdict
from glob import glob
from json import load
from operator import itemgetter
from os.path import abspath, dirname

from packaging.version import parse as parseVersion


def main() -> int:
    DIVISOR = "|:---|---:|---:|---:|---:|---:|---:|\n"
    ROOT_DIR = dirname(abspath(__file__))

    performance = []
    filenames = f"{ROOT_DIR}/../report/json/*.json"
    for file in sorted(glob(filenames)):
        with open(file, encoding="utf-8") as jfile:
            loaded = load(jfile)
            for item in loaded:
                item["version"] = parseVersion(item["version"])
            performance.extend(loaded)
    performance.sort(key=itemgetter("version", "command"))

    final = defaultdict(list)
    for item in performance:
        final[item.get("command")].append(
            {
                "version": item.get("version"),
                "mean": item.get("mean"),
                "median": item.get("median"),
                "memory": item.get("memory"),
            }
        )

    with open("support/compare.md", "w", encoding="utf-8") as file_to_save:
        file_to_save.write("### **Comparison**\n")
        # Mean
        file_to_save.write("\n")
        file_to_save.write("#### **Execution**\n")
        file_to_save.write("\n")
        file_to_save.write(
            "| Command |  Mean 3.6 [s] | Mean 3.7 [s] | Mean 3.8 [s] | Mean 3.9 [s] | Mean 3.10 [s] | Mean 3.11 [s] |\n"
        )
        file_to_save.write(DIVISOR)
        for command, items in final.items():
            file_to_save.write(f'| {command} | {" | ".join(str(item.get("mean", -1)) for item in items)} |\n')
        # Median
        file_to_save.write("\n")
        file_to_save.write(
            "| Command |  Median 3.6 [s] | Median 3.7 [s] | Median 3.8 [s] | Median 3.9 [s] | Median 3.10 [s] | Median 3.11 [s] |\n"
        )
        file_to_save.write(DIVISOR)
        for command, items in final.items():
            file_to_save.write(f'| {command} | {" | ".join(str(item.get("median", -1)) for item in items)} |\n')
        # Memory
        file_to_save.write("\n")
        file_to_save.write("#### **Memory Usage**\n")
        file_to_save.write("\n")
        file_to_save.write(
            "| Command |  MEM 3.6 [MB] | MEM 3.7 [MB] | MEM 3.8 [MB] | MEM 3.9 [MB] | MEM 3.10 [MB] | MEM 3.11 [MB] |\n"
        )
        file_to_save.write(DIVISOR)
        for command, items in final.items():
            file_to_save.write(f'| {command} | {" | ".join(str(item.get("memory", -1)) for item in items)} |\n')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
