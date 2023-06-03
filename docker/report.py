import sys
from collections import defaultdict
from glob import glob
from json import dumps, loads
from operator import itemgetter
from os import makedirs, popen
from statistics import mean


def main(version: str):
    # Load and parse performance stats generate by hyperfine
    performance = []
    filenames = "report/tmp/*part_%s.json" % version
    for file in sorted(glob(filenames)):
        with open(file, encoding="utf-8") as jfile:
            content = loads(jfile.read())
        content = content.get("results")[0]
        performance.append(
            {
                "version": version,
                "command": content.get("command", "").replace("python src/tests/", "").replace("src/tests/", ""),
                "executed": "yes" if content.get("mean", None) else "no",
                "mean": round(content.get("mean", -1), 5),
                "stddev": round(content.get("stddev", -1), 5),
                "median": round(content.get("median", -1), 5),
                "min": round(content.get("min", -1), 5),
                "max": round(content.get("max", -1), 5),
            }
        )
    performance = sorted(performance, key=itemgetter("command"))

    # Load and parse memory stats generate by mprof
    memory = defaultdict(list)
    filenames = "report/tmp/*_*part_%s.dat" % version
    for file in sorted(glob(filenames)):
        with open(file, "r", encoding="utf-8") as tfile:
            content = tfile.read().split("\n")
        command = content[0].strip().split("python ")[-1].replace("src/tests/", "")
        memory_usage = content[1:]
        for line in reversed(memory_usage):
            if not line:
                continue
            mem = float(line.replace("MEM", "").strip().split()[0])
            if mem > 0:
                memory[command].append(float(mem))
                break

    # Add memory usage to general performance stats
    for perf in performance:
        command = perf.get("command", "")
        perf["memory"] = round(mean(memory.get(command, [-1])), 5)

    # Get system information (num of cpus, memory, etc)
    system_state = "\n".join(
        [
            popen(cmd).read()
            for cmd in (
                "python --version",
                "uname -rsnpo",
                r"lscpu | egrep 'Model name|Thread|Core\(s\)|NUMA|CPU\(s\):|CPU max MHz:'",
                "cat /proc/meminfo | egrep 'MemTotal:|MemFree:|MemAvailable:'",
            )
        ]
    )

    # Save json data
    makedirs("report/json", exist_ok=True)
    with open("report/json/%s.json" % version, "w", encoding="utf-8") as file_to_save:
        file_to_save.write(dumps(performance, indent=4))

    # Save markdown report
    makedirs("report/markdown", exist_ok=True)
    with open("report/markdown/%s.md" % version, "w", encoding="utf-8") as file_to_save:
        file_to_save.write("### **Python %s**\n" % version)
        file_to_save.write("\n")
        file_to_save.write("```bash\n")
        file_to_save.write(system_state)
        file_to_save.write("```\n")
        file_to_save.write("\n")
        file_to_save.write(
            "| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |\n"
        )
        file_to_save.write("|:---|---:|---:|---:|---:|---:|---:|---:|\n")
        for item in performance:
            file_to_save.write(
                (
                    f"| `{item.get('command')}` | {item.get('executed')} | {item.get('mean')} | {item.get('stddev')} | "
                    f"{item.get('median')} | {item.get('min')} | {item.get('max')} | {item.get('memory')} |\n"
                )
            )

    return 0


if __name__ == "__main__":
    VERSION = str(sys.argv[1])
    raise SystemExit(main(version=VERSION))
