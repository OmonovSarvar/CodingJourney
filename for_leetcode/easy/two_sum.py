"""Two Sum (LeetCode) — problem description formatted clearly.

Given an array of integers `nums` and an integer `target`, return indices of the two
numbers such that they add up to `target`.

Assumptions:
- Exactly one solution exists.
- You may not use the same element twice.
- Return indices in any order.

Examples (doctest):
>>> two_sum([2, 7, 11, 15], 9)
[0, 1]

>>> two_sum([3, 2, 4], 6)
[1, 2]

>>> two_sum([3, 3], 6)
[0, 1]

Constraints:
- 2 <= len(nums) <= 10**4
- -10**9 <= nums[i], target <= 10**9
"""
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """Return indices of the two numbers that add up to target.

    Time: O(n), Space: O(n)
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    raise ValueError("No two sum solution")





