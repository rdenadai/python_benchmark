# @DONT_RUN

from typing import List, Tuple


def search(nums: List[int], target: int) -> Tuple[int]:
    d = dict(zip(nums, range(len(nums))))
    for i, num in enumerate(nums):
        k = d.get(target - num, None)
        if k and k != i:
            return i, k


def search_naive(nums: List[int], target: int) -> Tuple[int]:
    k, n1, n2 = 0, 0, 0
    for i, m in enumerate(nums):
        n = target - m
        sub_nums = nums[i + 1 :]
        if n in sub_nums:
            k = sub_nums.index(n) + (i + 1)
            if k != i:
                n1, n2 = i, k
                break
    return tuple(sorted((n1, n2)))
