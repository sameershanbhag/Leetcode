# Author: Sameer Shanbhag
# Leetcode Problem:
# https://leetcode.com/problems/is-subsequence
# Medium

from typing import List


class Solution0:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average = float('-inf')
        left = 0
        right = left + k

        current_sum = None
        while right <= len(nums):
            if current_sum is not None:
                current_sum = current_sum - nums[left - 1] + nums[right - 1]
            else:
                current_sum = sum(nums[left:right])
            max_average = max((current_sum / k), max_average)
            left += 1
            right += 1

        return max_average


if __name__ == '__main__':
    # Test Cases Basic
    inputs = [[[1, 12, -5, -6, 50, 3], 4], [[5], 1], [[0, 4, 0, 3, 2], 1], [[-1], 1]]

    sols = [12.75, 5, 4, -1]

    num_sol = 1

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(inputs):
            if solution.findMaxAverage(current[0], current[1]) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
