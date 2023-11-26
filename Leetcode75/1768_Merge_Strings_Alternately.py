# Author: Sameer Shanbhag
# Leetcode Problem:
# https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75
# Easy

from typing import List


class Solution0:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        counter = 0
        result = ""
        while counter < max(len(word1), len(word2)):
            if counter < len(word1):
                result += word1[counter]
            if counter < len(word2):
                result += word2[counter]
            counter += 1
        return result


if __name__ == '__main__':
    # Test Cases Basic
    words = [["abc", "pqr"], ["ab", "pqrs"], ["abcd", "pq"]]
    target = [9, 6, 6]

    sols = ["apbqcr", "apbqrs", "apbqcd"]

    num_sol = 1

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(words):
            if solution.mergeAlternately(current[0], current[1]) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
