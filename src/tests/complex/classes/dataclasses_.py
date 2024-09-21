# @ALLOWED_VERSIONS: 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13

from dataclasses import dataclass
from random import choice, randint


@dataclass
class Person:
    name: str
    age: int


def main():
    names = ("Rodolfo", "John", "Jane", "Doe", "Alice", "Bob", "Charlie", "David", "Eve", "Frank")
    persons = [Person(**{"name": choice(names), "age": randint(18, 65)}) for _ in range(20_000)]
    for person in persons:
        name, age = person.name, person.age
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
