# Author: Sameer Shanbhag
# Leetcode Problem: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Hard

from typing import List


class Solution0:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # O(n^2) Solution - using sorted

        # Final array
        final_nums = sorted(nums1 + nums2)
        len_fnums = len(final_nums)

        # initialize median
        median = 0

        # If the list is even
        if len_fnums % 2 == 0:
            median = (final_nums[len_fnums//2] + final_nums[len_fnums//2 - 1]) / 2
        else:
            median = final_nums[len_fnums//2]

        return median


class Solution1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # O(n) solution

        # Final array
        final_nums = []

        # initializing current counters
        nums1_counter = 0
        nums2_counter = 0

        # Merging the array with while loop
        while nums1_counter < len(nums1) or nums2_counter < len(nums2):
            # Merge the small to final list first
            if nums1_counter < len(nums1) and nums2_counter < len(nums2):
                if nums1[nums1_counter] < nums2[nums2_counter]:
                    final_nums.append(nums1[nums1_counter])
                    nums1_counter += 1

                elif nums1[nums1_counter] > nums2[nums2_counter]:
                    final_nums.append(nums2[nums2_counter])
                    nums2_counter += 1

                elif nums1[nums1_counter] == nums2[nums2_counter]:
                    final_nums.append(nums1[nums1_counter])
                    final_nums.append(nums2[nums2_counter])
                    nums1_counter += 1
                    nums2_counter += 1

            # If one of the array is exhausted append the other directly to final as both inputs are sorted
            if nums1_counter == len(nums1) and nums2_counter != len(nums2):
                final_nums.extend(nums2[nums2_counter:])
                break

            if nums2_counter == len(nums2) and nums1_counter != len(nums1):
                final_nums.extend(nums1[nums1_counter:])
                break

        len_fnums = len(final_nums)

        # If the list is even
        if len_fnums % 2 == 0:
            median = (final_nums[len_fnums//2] + final_nums[len_fnums//2 - 1]) / 2
        else:
            median = final_nums[len_fnums//2]

        return median


if __name__ == '__main__':
    # Test Cases Basic
    nums = [[[1, 3], [2]], [[1, 2], [3, 4]]]

    sols = [2.00000, 2.50000, 6]

    num_sol = 2

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(nums):
            if solution.findMedianSortedArrays(current[0], current[1]) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
