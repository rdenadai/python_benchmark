# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11

from typing import List, Tuple

from utils import search


def two_sum(nums: List[int], target: int) -> Tuple[int]:
    return search(nums, target)


if __name__ == "__main__":
    assert two_sum([3, 3], 6) == (0, 1)
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([3, 2, 4], 6) == (1, 2)
    assert two_sum([-1, -2, -3, -4, -5], -8) == (2, 4)
    assert two_sum([3, 10, 1, 5, 9, 2, 8, 1000, 3000, 3199], 3200) == (2, 9)
    assert two_sum([4000, 500, 1, 8000, 8001, 3, 10, 5, 9, 2, 8, 1100, 3000, 3199], 3200) == (2, 13)
    assert two_sum(
        [
            0,
            1,
            2,
            399,
            156,
            37,
            4000,
            400,
            401,
            500,
            8000,
            8001,
            3,
            10,
            5,
            9,
            2,
            8,
            1100,
            3000,
            3199,
            8111,
            8122,
            537,
            800,
        ],
        3200,
    ) == (
        1,
        20,
    )
