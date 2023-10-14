# Author: Sameer Shanbhag
# Leetcode Problem: https://leetcode.com/problems/product-of-array-except-self/
# Medium

from typing import List


class Solution0:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n^2) Solution

        # initialize return list
        product = []

        for idx, current_number in enumerate(nums):
            final_product = 1
            for sec_num in nums[0:idx] + nums[idx+1:]:
                final_product *= sec_num
            product.append(final_product)

        return product


class Solution1:
    def productExceptSelf(self, nums: List[int]) -> list:
        # O(n) Solution
        prefix_product = 1
        suffix_product = 1

        result = [1]*len(nums)

        # Divide the problem statement into two pieces

        # Finding the prefix product at each element and storing it
        # in result
        for idx, current_number in enumerate(nums):
            result[idx] = prefix_product
            prefix_product *= current_number

        # Finding the suffix product at each element and storing it
        # in result
        for idx in range(len(nums)-1, -1, -1):
            result[idx] *= suffix_product
            suffix_product *= nums[idx]

        return result


if __name__ == '__main__':
    # Test Cases Basic
    nums = [[1, 2, 3, 4], [-1, 1, 0, -3, 3]]

    sols = [[24, 12, 8, 6], [0, 0, 9, 0, 0]]

    num_sol = 2

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(nums):
            if solution.productExceptSelf(current) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
