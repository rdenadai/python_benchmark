# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11

from datetime import datetime
from json import dumps, loads
from random import choice, randint

NAMES = (
    "Rodolfo",
    "Sthefany",
    "Larissa",
    "Rodrigo",
)


def main():
    names = NAMES  # pylint(loop-global-usage)
    for _ in range(30_000):
        dumped = dumps(
            {
                "name": choice(names),
                "age": randint(5, 75),
                "city": "São Paulo",
                "datetime": datetime.now().isoformat(),
            }
        )
        loaded = loads(dumped)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
