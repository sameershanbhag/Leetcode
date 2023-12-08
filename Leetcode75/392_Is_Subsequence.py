# Author: Sameer Shanbhag
# Leetcode Problem:
# https://leetcode.com/problems/is-subsequence
# Easy

class Solution0:
    def isSubsequence(self, s: str, t: str) -> bool:
        counter = 0
        for i in t:
            if counter >= len(s):
                return True

            if i == s[counter]:
                counter += 1

        if counter >= len(s):
            return True

        return False


if __name__ == '__main__':
    # Test Cases Basic
    inputs = [["abc", "ahbgdc"], ["axc", "ahbgdc"], ["", "ahbgdc"], ["abc", ""]]

    sols = [True, False, True, False]

    num_sol = 1

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(inputs):
            if solution.isSubsequence(current[0], current[1]) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
