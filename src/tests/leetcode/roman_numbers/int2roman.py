from math import log10
from sys import setrecursionlimit

setrecursionlimit(10_000)

ROMAN_INT: dict[int, str] = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M",
    5000: "V̅",
    10000: "X̅",
}


def int_to_roman(num: int) -> str:
    if num <= 0:
        return ""

    dec = int(log10(num)) + 1
    mult = int(f"1{'0' * (dec-1)}")
    rec = int_to_roman(num % mult)

    if num < (4 * mult):
        return f"{ROMAN_INT.get(mult) * (num // mult)}{rec}"

    mult5 = 5 * mult
    if (4 * mult) <= num < mult5:
        return f"{ROMAN_INT.get(mult)}{ROMAN_INT.get(mult5)}{rec}"

    if mult5 <= num < (6 * mult):
        return f"{ROMAN_INT.get(mult5)}{rec}"

    if num < (9 * mult):
        qtd = (num // mult) % 5
        return f"{ROMAN_INT.get(mult5)}{ROMAN_INT.get(mult) * qtd}{rec}"

    return f"{ROMAN_INT.get(mult)}{ROMAN_INT.get(mult * 10)}{rec}"


def main():
    assert int_to_roman(3) == "III"
    assert int_to_roman(4) == "IV"
    assert int_to_roman(6) == "VI"
    assert int_to_roman(8) == "VIII"
    assert int_to_roman(9) == "IX"
    assert int_to_roman(10) == "X"
    assert int_to_roman(12) == "XII"
    assert int_to_roman(19) == "XIX"
    assert int_to_roman(21) == "XXI"
    assert int_to_roman(40) == "XL"
    assert int_to_roman(41) == "XLI"
    assert int_to_roman(58) == "LVIII"
    assert int_to_roman(75) == "LXXV"
    assert int_to_roman(95) == "XCV"
    assert int_to_roman(99) == "XCIX"
    assert int_to_roman(100) == "C"
    assert int_to_roman(251) == "CCLI"
    assert int_to_roman(500) == "D"
    assert int_to_roman(600) == "DC"
    assert int_to_roman(999) == "CMXCIX"
    assert int_to_roman(1000) == "M"
    assert int_to_roman(1200) == "MCC"
    assert int_to_roman(1994) == "MCMXCIV"
    assert int_to_roman(2021) == "MMXXI"
    assert int_to_roman(2020) == "MMXX"
    assert int_to_roman(3999) == "MMMCMXCIX"
    assert int_to_roman(10_000) == "X̅"
    assert int_to_roman(10_001) == "X̅I"
    assert int_to_roman(10_101) == "X̅CI"


if __name__ == "__main__":
    main()
