# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11

from typing import NamedTuple


class Person(NamedTuple):
    name: str
    age: int

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"

    def __repr__(self) -> str:
        return f"Person(name={self.name!r}, age={self.age!r})"


def main():
    persons = [Person("Rodolfo", 40) for _ in range(20_000)]
    for person in persons:
        name, age = person.name, person.age
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
