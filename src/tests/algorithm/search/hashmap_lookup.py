# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12

from random import choice
from typing import Generator

from faker import Faker


def generate_data() -> Generator:
    fake = Faker("pt_BR")
    return (fake.name() for _ in range(50_000))


def main():
    names: list[str] = list(sorted(set(generate_data())))
    dnames: dict[str] = {name: idx for idx, name in enumerate(names)}
    for _ in range(100):
        search: str = choice(names)
        idx = dnames.get(search, None)
        assert search == names[idx]

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
