# Author: Sameer Shanbhag
# Leetcode Problem:
# https://leetcode.com/problems/reverse-vowels-of-a-string
# Easy

class Solution0:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1

        s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        while left <= right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] in vowels and s[right] not in vowels:
                right -= 1
            elif s[right] in vowels and s[left] not in vowels:
                left += 1
            elif s[left] not in vowels and s[right] not in vowels:
                left += 1
                right -= 1
        return "".join(s)


if __name__ == '__main__':
    # Test Cases Basic
    vowel_check = ["hello", "leetcode", "aA", "a", ""]

    sols = ["holle", "leotcede", "Aa", "a", ""]

    num_sol = 1

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(vowel_check):
            if solution.reverseVowels(current) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
