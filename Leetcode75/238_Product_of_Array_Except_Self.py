# Author: Sameer Shanbhag
# Leetcode Problem: https://leetcode.com/problems/product-of-array-except-self/
# Medium
from typing import List


class Solution0:
    def productExceptSelf(self, nums: List[int]) -> list:
        prefix_product = 1
        suffix_product = 1

        sol = [0] * (len(nums))

        for i in range(len(nums)):
            sol[i] = prefix_product
            prefix_product *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            sol[i] *= suffix_product
            suffix_product *= nums[i]

        return sol


if __name__ == '__main__':
    # Test Cases Basic
    nums = [[1, 2, 3, 4], [-1, 1, 0, -3, 3]]

    sols = [[24, 12, 8, 6], [0, 0, 9, 0, 0]]

    num_sol = 1

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(nums):
            if solution.productExceptSelf(current) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
