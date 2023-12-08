# Author: Sameer Shanbhag
# Leetcode Problem:
# https://leetcode.com/problems/find-the-difference-of-two-arrays/
# Easy

from typing import List


class Solution0:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        sol = [[], []]

        for i in nums1:
            if i not in nums2:
                sol[0].append(i)
            else:
                nums2.remove(i)

        sol[1].extend(list(nums2))
        return sol


class Solution1:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        return [list(nums1.difference(nums2)), list(nums2.difference(nums1))]


if __name__ == '__main__':
    # Test Cases Basic
    inputs = [[[1, 2, 3], [2, 4, 6]], [[1, 2, 3], [2, 3, 4]], [[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [4, 5, 6]]]

    sols = [[[1, 3], [4, 6]], [[1], [4]], [[], []], [[1, 2, 3], [4, 5, 6]]]

    num_sol = 2

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(inputs):
            if solution.findDifference(current[0], current[1]) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
