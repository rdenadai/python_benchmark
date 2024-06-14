ROMAN_INT = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def roman_to_int(s: str) -> int:
    total = 0
    remove_previous = 0

    size = len(s) - 1
    for i in range(size + 1):
        val = ROMAN_INT.get(s[i], 0)
        if i < size and val < ROMAN_INT.get(s[i + 1], 0):
            remove_previous = val
        else:
            total += val - remove_previous
            remove_previous = 0
    return total


def main():
    assert roman_to_int("III") == 3
    assert roman_to_int("IV") == 4
    assert roman_to_int("VI") == 6
    assert roman_to_int("VIII") == 8
    assert roman_to_int("IX") == 9
    assert roman_to_int("LVIII") == 58
    assert roman_to_int("MCMXCIV") == 1994
    assert roman_to_int("MMXXI") == 2021
    assert roman_to_int("MMXX") == 2020


if __name__ == "__main__":
    main()
