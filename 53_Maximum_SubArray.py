# Author: Sameer Shanbhag
# Leetcode Problem: https://leetcode.com/problems/maximum-subarray/
# Medium

from typing import List


class Solution0:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(n) Solution
        global_max, current_sum = 0, 0

        # Kadens Algorithm
        for idx, current_number in enumerate(nums):
            current_sum += current_number

            if current_sum > global_max:
                global_max = current_sum

            if current_sum < 0:
                current_sum = 0

        return global_max


if __name__ == '__main__':
    # Test Cases Basic
    nums = [[-2, 1, -3, 4, -1, 2, 1, -5, 4], [1], [5, 4, -1, 7, 8]]

    sols = [6, 1, 23]

    num_sol = 1

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(nums):
            if solution.maxSubArray(current) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
