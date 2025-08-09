# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13, 3.14


def main() -> int:
    for _ in range(100_000):
        for i in range(100):
            _ = i * i
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
