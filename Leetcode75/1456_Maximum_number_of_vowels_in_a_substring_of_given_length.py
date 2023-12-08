# Author: Sameer Shanbhag
# Leetcode Problem:
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length
# Medium

from typing import List


class Solution0:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        max_vowels = 0
        current_max = 0

        left = 0
        right = left + k

        while right <= len(s):
            if max_vowels == 0:
                for i in s[left:right]:
                    if i in vowels:
                        max_vowels += 1
                current_max = max_vowels
            else:
                if s[left - 1] in vowels:
                    current_max -= 1
                if s[right - 1] in vowels:
                    current_max += 1
                max_vowels = max(max_vowels, current_max)
            left += 1
            right += 1

        return max_vowels


if __name__ == '__main__':
    # Test Cases Basic
    inputs = [["abciiidef", 3], ["aeiou", 2], ["leetcode", 3], ["rhythms", 4]]

    sols = [3, 2, 2, 0]

    num_sol = 1

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(inputs):
            if solution.maxVowels(current[0], current[1]) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
