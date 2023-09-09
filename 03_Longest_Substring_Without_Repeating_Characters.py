# Author: Sameer Shanbhag
# Leetcode Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Medium

class Solution0:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0

        # O(n^2) Solution
        final_max = 0

        # Iterate through the main list
        for init_itr in range(len(s)):
            seen = {s[init_itr]: True}
            current_max = 1

            # Iterate through the list until we find seen
            for idx, internal in enumerate(s[init_itr + 1:]):
                if s[init_itr] == internal or internal in seen:
                    final_max = current_max if final_max < current_max else final_max
                    break

                current_max += 1
                if init_itr + idx + 1 == len(s) - 1:
                    final_max = current_max if final_max < current_max else final_max
                    break

                seen[internal] = True

        return final_max if final_max > 0 else 1


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(n) Solution
        n = len(s)

        # Initialize result
        result = 0

        # initialize current copy pointer
        cptr = 0

        # Initialize Character List
        character_list = {}

        for idx in range(n):
            # check if duplicate is found
            if s[idx] in character_list:
                # as there is a match set the cptr to last index of repeating char
                cptr = max(cptr, character_list[s[idx]])

            # Update the result with the max of old result vs current max ie idx - cptr + 1
            result = max(result, idx - cptr + 1)

            # Update the character list to update the value of character in the dictionary
            character_list[s[idx]] = idx + 1

        return result


if __name__ == '__main__':
    # Test Cases Basic
    strs = ['abcabcbb', 'bbbbb', 'pwwkew', 'b', 'au']
    sols = [3, 1, 3, 1, 2]

    num_sol = 2

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(strs):
            if solution.lengthOfLongestSubstring(current) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
