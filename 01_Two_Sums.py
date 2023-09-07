# Author: Sameer Shanbhag
# Leetcode Problem: https://leetcode.com/problems/two-sum/
# Easy

from typing import List


class Solution0:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return [0, 0]

        # Initial Implementation O(n^2)
        for idx, first in enumerate(nums):
            for idx_second, second in enumerate(nums[idx + 1:]):
                if first + second == target:
                    return [idx, idx + 1 + idx_second]


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return [0, 0]

        # O(n) implementation
        nums_map = {}

        for idx, element in enumerate(nums):
            diff = target - element
            if diff in nums_map:
                return [nums_map[diff], idx]
            else:
                nums_map[element] = idx

        return [-1, -1]


if __name__ == '__main__':
    # Test Cases Basic
    nums = [[2, 7, 11, 15], [3, 2, 4], [3, 3]]
    target = [9, 6, 6]

    sols = [[0, 1], [1, 2], [0, 1]]

    num_sol = 2

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(nums):
            if solution.twoSum(current, target[j]) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
