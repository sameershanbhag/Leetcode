# Author: Sameer Shanbhag
# Leetcode Problem:
# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Easy

class Solution0:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Generate a set of all the possible soulutions
        current_greatest = set()
        # Iterate over the length of second string as it is concatenation for the first string
        for idx in range(len(str2)):
            # Check if the current string is a divisor of both the strings
            if len(str1.replace(str2[:idx+1], '')) == 0 and len(str2.replace(str2[:idx+1], '')) == 0:
                # If yes, add it to the set
                current_greatest.add(str2[:idx+1])
        # Return the max of the set if the set is not empty
        if len(current_greatest):
            return max(current_greatest)
        return ""


if __name__ == '__main__':
    # Test Cases Basic
    words = [["ABCABC", "ABC"], ["ABABAB", "ABAB"], ["LEET", "CODE"]]

    sols = ["ABC", "AB", ""]

    num_sol = 1

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(words):
            if solution.gcdOfStrings(current[0], current[1]) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
