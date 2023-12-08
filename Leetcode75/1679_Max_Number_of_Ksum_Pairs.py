# Author: Sameer Shanbhag
# Leetcode Problem:
# https://leetcode.com/problems/is-subsequence
# Medium

from typing import List


class Solution0:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums.sort()  # Do this to maintain the two pointers

        left = 0
        right = len(nums) - 1
        ops = 0

        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                ops += 1
            elif nums[left] + nums[right] > k:
                right -= 1  # As the sum is more minimize the bigger number
            else:
                left += 1  # As the sum is less maximize the smaller number
        return ops


if __name__ == '__main__':
    # Test Cases Basic
    inputs = [[[1, 2, 3, 4], 5], [[3, 1, 3, 4, 3], 6], [[1, 1, 1, 1], 2], [[1, 2, 3], 3]]

    sols = [2, 1, 2, 1]

    num_sol = 1

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(inputs):
            if solution.maxOperations(current[0], current[1]) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
