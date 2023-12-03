# Author: Sameer Shanbhag
# Leetcode Problem:
# https://leetcode.com/problems/reverse-words-in-a-string
# Easy

class Solution0:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split(" ")
        word_list = [*s[::-1]]
        new_word = ""

        for i in word_list:
            if len(i.strip()):
                new_word += f" {i.strip()}"

        return new_word.strip()


if __name__ == '__main__':
    # Test Cases Basic
    vowel_check = ["the sky is blue", "  hello world  ", "a good   example"]

    sols = ["blue is sky the", "world hello", "example good a"]

    num_sol = 1

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(vowel_check):
            if solution.reverseWords(current) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
