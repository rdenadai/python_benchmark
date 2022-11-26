# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11

from os.path import abspath, dirname

from pandas import read_csv


def main():
    ROOT_DIR = dirname(abspath(__file__))
    dataframe = read_csv(f"{ROOT_DIR}/../../../data/titanic.csv", encoding="utf-8", delimiter=",", quotechar='"')
    data = [row.to_dict() for _, row in dataframe.iterrows()]
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
