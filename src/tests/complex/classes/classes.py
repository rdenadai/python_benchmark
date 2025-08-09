# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13, 3.14

from random import choice, randint


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"

    def __repr__(self) -> str:
        return f"Person(name={self.name!r}, age={self.age!r})"


def main():
    names = ("Rodolfo", "John", "Jane", "Doe", "Alice", "Bob", "Charlie", "David", "Eve", "Frank")
    persons = [Person(**{"name": choice(names), "age": randint(18, 65)}) for _ in range(20_000)]
    for person in persons:
        name, age = person.name, person.age
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
