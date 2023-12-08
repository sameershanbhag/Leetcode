# Author: Sameer Shanbhag
# Leetcode Problem:
# https://leetcode.com/problems/find-the-highest-altitude
# Easy

from typing import List


class Solution0:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0

        current_alt = 0

        for alt_gain in gain:
            current_alt += alt_gain
            highest = max(current_alt, highest)

        return highest


if __name__ == '__main__':
    # Test Cases Basic
    inputs = [[-5, 1, 5, 0, -7], [-4, -3, -2, -1, 4, 3, 2], [1, 2, 3, 4, 5], [5, 6, 7, 8, 9]]

    sols = [1, 0, 15, 35]

    num_sol = 1

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(inputs):
            if solution.largestAltitude(current) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
