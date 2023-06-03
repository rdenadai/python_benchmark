# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11

import sqlite3
from os.path import abspath, dirname

from pandas import read_csv


def main():
    ROOT_DIR = dirname(abspath(__file__))
    dataframe = read_csv(f"{ROOT_DIR}/../../../data/titanic.csv", encoding="utf-8", delimiter=",", quotechar='"')

    with sqlite3.connect("file:cachedb?mode=memory&cache=shared") as conn:
        dataframe.to_sql("titanic", conn, if_exists="replace")
        cur = conn.cursor()
        res = cur.execute("SELECT COUNT(*) FROM titanic")
        res = res.fetchone()[0]
        cur.close()
        assert res == 891
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
