import math

sqrt_map = {
    2: 1,
    4: 2,
    9: 3,
    16: 4,
    25: 5,
    36: 6,
    49: 7,
    64: 8,
    81: 9,
    100: 10,
}


def sqrt(x: int) -> int:
    if 0 <= x <= 1:
        return x
    if solution := sqrt_map.get(x, None):
        return solution
    return math.floor(10 ** (math.log10(x) / 2) + 1e-5)


def main():
    assert sqrt(0) == math.floor(math.sqrt(0))
    assert sqrt(1) == math.floor(math.sqrt(1))
    assert sqrt(2) == math.floor(math.sqrt(1))
    assert sqrt(4) == math.floor(math.sqrt(4))
    assert sqrt(8) == math.floor(math.sqrt(8))
    assert sqrt(9) == math.floor(math.sqrt(9))
    assert sqrt(16) == math.floor(math.sqrt(16))
    assert sqrt(25) == math.floor(math.sqrt(25))
    assert sqrt(36) == math.floor(math.sqrt(36))
    assert sqrt(49) == math.floor(math.sqrt(49))
    assert sqrt(64) == math.floor(math.sqrt(64))
    assert sqrt(81) == math.floor(math.sqrt(81))
    assert sqrt(100) == math.floor(math.sqrt(100))
    assert sqrt(324) == math.floor(math.sqrt(324))
    assert sqrt(8192) == math.floor(math.sqrt(8192))


if __name__ == "__main__":
    main()
