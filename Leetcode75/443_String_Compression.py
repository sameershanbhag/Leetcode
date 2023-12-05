# Author: Sameer Shanbhag
# Leetcode Problem: https://leetcode.com/problems/string-compression
# Medium
from typing import List


class Solution0:
    def compress(self, chars: List[str]) -> int:
        group_char = chars.pop(0) + "1"
        b = len(chars)
        while b:
            i = chars.pop(0)
            b -= 1
            if group_char[0] == i:
                group_char = group_char[0] + str(int(group_char[1:]) + 1)
            else:
                chars.append(group_char[0])
                if int(group_char[1:]) != 1:
                    chars.extend(list(group_char[1:]))
                group_char = i + "1"

        # Takes care of the last group
        chars.append(group_char[0])
        if int(group_char[1:]) != 1:
            chars.extend(list(group_char[1:]))
        return len(chars)


if __name__ == '__main__':
    # Test Cases Basic
    nums = [["a", "a", "b", "b", "c", "c", "c"], ["a"],
            ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]]

    sols = [["a", "2", "b", "2", "c", "3"], ["a"], ["a", "b", "1", "2"]]

    num_sol = 1

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(nums):
            if solution.compress(current) == len(sols[j]) and current == sols[j]:
                print("PASS")
            else:
                print("FAIL")
