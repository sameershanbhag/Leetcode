# Author: Sameer Shanbhag
# Leetcode Problem: https://leetcode.com/problems/maximum-subarray/
# Medium

from typing import List


class Solution0:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(n) Solution Kadens Algorithms
        global_max, current_sum = float("-inf"), 0

        for idx, current_number in enumerate(nums):
            current_sum += current_number

            global_max = max(global_max, current_sum)

            current_sum = max(current_sum, 0)

        return global_max


class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(n) solution DP
        current_array = [nums[0]]

        max_sum = current_array[0]

        for i in range(1, len(nums)):
            current_array.append(max(current_array[i - 1] + nums[i], nums[i]))

            if max_sum < current_array[i]:
                max_sum = current_array[i]

        return max_sum


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        # Divide and conquer solution
        def dac(cur_numbers):
            if len(cur_numbers) == 1:
                return cur_numbers[0]

            mid = len(cur_numbers) // 2
            max_left = dac(cur_numbers[:mid])
            max_right = dac(cur_numbers[mid:])

            left_sum = float('-inf')
            sum = 0
            for i in range(mid-1, -1, -1):
                sum += cur_numbers[i]
                left_sum = max(left_sum, sum)

            right_sum = float('-inf')
            sum = 0
            for i in range(mid, len(cur_numbers)):
                sum += cur_numbers[i]
                right_sum = max(right_sum, sum)

            cross_over = left_sum + right_sum

            return max(max_left, max_right, cross_over)

        return dac(nums)


if __name__ == '__main__':
    # Test Cases Basic
    nums = [[-2, 1, -3, 4, -1, 2, 1, -5, 4], [1], [5, 4, -1, 7, 8]]

    sols = [6, 1, 23]

    num_sol = 3

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(nums):
            if solution.maxSubArray(current) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
