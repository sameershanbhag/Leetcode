# Author: Sameer Shanbhag
# Leetcode Problem:
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
# Medium

from typing import List


class Solution0:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        while left < right:
            max_water = max((min(height[left], height[right]) * (right - left)), max_water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water


if __name__ == '__main__':
    # Test Cases Basic
    inputs = [[1, 8, 6, 2, 5, 4, 8, 3, 7], [1, 1], [4, 3, 2, 1, 4], [1, 2, 1]]

    sols = [49, 1, 16, 2]

    num_sol = 1

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(inputs):
            if solution.maxArea(current) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
