# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13

import io
import re
from collections import Counter
from os.path import abspath, dirname


def count_words(text: str) -> int:
    words = re.findall(r"\b\w+\b", text.lower())
    word_counts = Counter(words)
    return sum(word_counts.values())


def main() -> int:
    ROOT_DIR = dirname(abspath(__file__))
    with io.open(f"{ROOT_DIR}/../../../data/python.txt") as file:
        text = file.read()
    for _ in range(25):
        _ = count_words(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
