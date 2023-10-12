# Author: Sameer Shanbhag
# Leetcode Problem: https://leetcode.com/problems/contains-duplicate/
# Easy

from typing import List


class Solution0:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(n^2) Solution

        for idx, current_number in enumerate(nums):
            for second_number in nums[idx + 1:]:
                if second_number == current_number:
                    return True

        return False


class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(nlogn) solution with Binary Search

        # NOTE: This solution will not work in Leetcode because its slow
        # Binary search to search for the data
        def binary_search(nums, target) -> bool:
            array_len = len(nums)

            if not array_len:
                return False

            if array_len == 1:
                return nums[0] == target

            return binary_search(nums[:array_len//2], target) or binary_search(nums[array_len//2:], target)

        for idx, current_number in enumerate(nums):
            if binary_search(nums[idx + 1:], current_number):
                return True

        return False


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(n) solution with Set (HASH)

        num_index = set()
        for idx, current_number in enumerate(nums):
            if current_number in num_index:
                return True
            else:
                num_index.add(current_number)

        return False


if __name__ == '__main__':
    # Test Cases Basic
    nums = [[1, 2, 3, 1], [1, 2, 3, 4], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]

    sols = [True, False, True]

    num_sol = 3

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(nums):
            if solution.containsDuplicate(current) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
