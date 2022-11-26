# @ALLOWED_VERSIONS: 3.7, 3.8, 3.9, 3.10, 3.11

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


def main():
    persons = [Person("Rodolfo", 40) for _ in range(20_000)]
    for person in persons:
        name, age = person.name, person.age
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
