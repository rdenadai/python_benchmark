# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13, 3.14

from copy import deepcopy
from random import randint


def naive_bubble_sort(lst: list) -> None:
    n = len(lst) - 1
    if n <= 0:
        return

    i, is_sorted = 0, True
    while True:
        if i >= n:
            if is_sorted:
                break
            i, is_sorted = 0, True

        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            is_sorted = False
        i += 1


def main() -> None:
    lst = [3, 1, 9, 5]
    naive_bubble_sort(lst)
    assert lst == [1, 3, 5, 9]

    lst = [7, 2, 0, 4, 8, 6]
    naive_bubble_sort(lst)
    assert lst == [0, 2, 4, 6, 7, 8]

    lst = [1]
    naive_bubble_sort(lst)
    assert lst == [1]

    lst = []
    naive_bubble_sort(lst)
    assert lst == []

    lst = [10, 5, 18, 19, 30, 25, 20, 15, 40, 100, 99, 76, 78, 80]
    c_list = deepcopy(lst)
    naive_bubble_sort(lst)
    c_list.sort()
    assert lst == c_list

    lst = list({randint(0, 10_000) for _ in range(5_000)})
    c_list = deepcopy(lst)
    naive_bubble_sort(lst)
    c_list.sort()
    assert lst == c_list


if __name__ == "__main__":
    main()
