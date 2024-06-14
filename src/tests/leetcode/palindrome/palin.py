def isalnum(c):
    c = ord(c)
    return 48 <= c <= 57 or 65 <= c <= 90 or 97 <= c <= 122


def is_palindrome(s: str | None) -> bool:
    s = "".join(c for c in s or "" if isalnum(c)).lower()
    return s == s[::-1]


def main() -> None:
    assert is_palindrome(" ") == True
    assert is_palindrome("") == True
    assert is_palindrome(None) == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("never odd or even") == True
    assert is_palindrome("0P") == False
    assert is_palindrome(".,") == True


if __name__ == "__main__":
    main()
