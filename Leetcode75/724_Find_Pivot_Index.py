# Author: Sameer Shanbhag
# Leetcode Problem:
# https://leetcode.com/problems/find-pivot-index
# Easy

from typing import List


class Solution0:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = 0

        for i in nums:
            total_sum += i

        left_sum = 0

        for idx, current in enumerate(nums):
            if left_sum * 2 == total_sum - current:
                return idx
            left_sum += current

        return -1


if __name__ == '__main__':
    # Test Cases Basic
    inputs = [[1, 7, 3, 6, 5, 6], [1, 2, 3], [2, 1, -1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

    sols = [3, -1, 0, -1]

    num_sol = 1

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(inputs):
            if solution.pivotIndex(current) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
