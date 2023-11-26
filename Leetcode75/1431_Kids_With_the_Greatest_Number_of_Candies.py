# Author: Sameer Shanbhag
# Leetcode Problem:
# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Easy
from typing import List


class Solution0:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Generate a set of all the possible solutions
        max_candies = max(candies)
        # Return True if the current candy + extra candies is greater than or equal to the max
        return [True if x + extraCandies >= max_candies else False for x in candies]


if __name__ == '__main__':
    # Test Cases Basic
    words = [[[4, 2, 1, 1, 2], 1], [[2, 3, 5, 1, 3], 3], [[12, 1, 12], 10]]

    sols = [[True, False, False, False, False], [True, True, True, False, True], [True, False, True]]

    num_sol = 1

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(words):
            if solution.kidsWithCandies(current[0], current[1]) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
