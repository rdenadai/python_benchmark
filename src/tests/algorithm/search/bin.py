# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13, 3.14

from random import choice
from typing import Generator

from faker import Faker


def generate_data() -> Generator:
    fake = Faker("pt_BR")
    return (fake.name() for _ in range(50_000))


def bin_search(name, names):
    low, high = 0, len(names)
    while high - low > 0:
        mid = (high + low) // 2
        selected = names[mid]
        if name == selected:
            return mid
        elif name > selected:
            low = mid + 1
        else:
            high = mid


def main():
    names: list[str] = list(sorted(set(generate_data())))
    for _ in range(100):
        search: str = choice(names)
        idx = bin_search(search, names)
        assert search == names[idx]

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
