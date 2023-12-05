# Author: Sameer Shanbhag
# Leetcode Problem:
# https://leetcode.com/problems/reverse-vowels-of-a-string
# Easy
from typing import List


class Solution0:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 1

        while right < len(nums):
            # We never check for any other number on the left pointer
            if nums[left] != 0:
                left += 1
                right += 1
            elif nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
            elif nums[left] == 0 and nums[right] == 0:
                right += 1


if __name__ == '__main__':
    # Test Cases Basic
    vowel_check = [[0, 1, 0, 3, 12], [0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], []]

    sols = [[1, 3, 12, 0, 0], [0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], []]

    num_sol = 1

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(vowel_check):
            solution.moveZeroes(current)
            if current == sols[j]:
                print("PASS")
            else:
                print("FAIL")
