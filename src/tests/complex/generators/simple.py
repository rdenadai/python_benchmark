# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13


def gen():
    for _ in range(100_000):
        yield {"name": "generator"}


def main():
    _ = list(v for v in gen())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
