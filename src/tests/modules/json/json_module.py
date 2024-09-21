# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13

from datetime import datetime
from json import dumps, loads
from random import choice, randint

NAMES = ("Rodolfo", "John", "Jane", "Doe", "Alice", "Bob", "Charlie", "David", "Eve", "Frank")


def main():
    names = NAMES  # pylint(loop-global-usage)
    for _ in range(30_000):
        dumped = dumps(
            {
                "name": choice(names),
                "age": randint(18, 65),
                "city": "Sao Paulo",
                "datetime": datetime.now().isoformat(),
            }
        )
        _ = loads(dumped)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
