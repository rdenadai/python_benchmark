# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13

from csv import DictReader
from os.path import abspath, dirname


def main():
    ROOT_DIR = dirname(abspath(__file__))
    with open(f"{ROOT_DIR}/../../../data/titanic.csv", encoding="utf-8", newline="") as csvfile:
        csv_reader = DictReader(csvfile, delimiter=",", quotechar='"')
        _ = [row for row in csv_reader]
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
