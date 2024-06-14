# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13

import io
from os.path import abspath, dirname
from re import MULTILINE, findall, sub
from string import digits, punctuation
from typing import Tuple

RM = (
    (r"(http[s]*?:\/\/)+.*[\r\n]*", r""),
    (r"@", r""),
    (r"\n+", r" . "),
    (r'"', r" "),
    (r"\'", r" "),
    (r"#", r""),
    (r"(RT)", r""),
    (r"[…]", " . "),
    (r"[0-9]*", r""),
    (r"“", r""),
    (r"”", ""),
    (r"([aeiouqwtyupdfghjklçzxcvbnm|!@$%&\.\[\]\(\)+-_=<>,;:])\1+", r"\1"),
    (r"(\bñ\n)", "não"),
    (r"(nã)", "não"),
    (r"\s+", r" "),
    (r"(nãoo)", "não"),
)


def clean_up(text: str) -> Tuple[str, ...]:
    text = text.lower()
    for punct in punctuation + digits:
        text = text.replace(punct, " ")
    for pattern, replace in RM:
        text = sub(pattern, replace, text, flags=MULTILINE)
    words = findall(r"\b\w+\b", text)
    return tuple(word for word in words if len(word) > 2)


def uniq_words(words: Tuple[str, ...]) -> Tuple[str, ...]:
    return tuple(sorted(set(words)))


def main() -> int:
    ROOT_DIR = dirname(abspath(__file__))
    with io.open(f"{ROOT_DIR}/../../../data/python.txt") as file:
        text = file.read()
    for _ in range(25):
        _ = uniq_words(clean_up(text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
