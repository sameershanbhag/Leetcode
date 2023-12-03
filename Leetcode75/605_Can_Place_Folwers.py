# Author: Sameer Shanbhag
# Leetcode Problem:
# https://leetcode.com/problems/can-place-flowers/
# Easy
from typing import List


class Solution0:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if n == 0:
                return True
            if flowerbed[i] == 0:
                if i == 0 and i + 1 < len(flowerbed):
                    if flowerbed[i + 1] == 0:
                        n -= 1
                        flowerbed[i] = 1
                elif i == len(flowerbed) - 1:
                    if flowerbed[i - 1] == 0:
                        n -= 1
                elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    n -= 1
                    flowerbed[i] = 1
            if n == 0:
                return True

        return False


if __name__ == '__main__':
    # Test Cases Basic
    flowerbed_ques = [[[1, 0, 0, 0, 1], 1], [[1, 0, 0, 0, 1], 2]]

    sols = [True, False]

    num_sol = 1

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(flowerbed_ques):
            if solution.canPlaceFlowers(current[0], current[1]) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
