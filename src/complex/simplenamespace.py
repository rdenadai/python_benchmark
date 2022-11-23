# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11

from types import SimpleNamespace


def main():
    for _ in range(100):
        person = SimpleNamespace(**{"name": "Rodolfo", "age": 39})
        name, age = person.name, person.age
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
