# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13

from os.path import abspath, dirname

ROOT_DIR = dirname(abspath(__file__))


def readlines(filename):
    with open(filename, encoding="utf-8", newline="") as f:
        for line in f:
            yield line


def main() -> int:
    filename = f"{ROOT_DIR}/../../../data/IMDb_Dataset.csv"
    _ = sum(len(line) for line in readlines(filename))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
