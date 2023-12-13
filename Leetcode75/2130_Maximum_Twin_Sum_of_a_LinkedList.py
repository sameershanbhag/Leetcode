# Author: Sameer Shanbhag
# Leetcode Problem:
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list
# Medium
from typing import Optional

from ListNode import ListNode


class Solution0:
    def pairSum(self, head: Optional[ListNode]) -> int:
        current_array = []

        while head:
            current_array.append(head.val)
            head = head.next

        n = len(current_array)

        max_sum = float("-inf")

        for i in range(0, n // 2):
            max_sum = max(max_sum, current_array[i] + current_array[n - 1 - i])

        return max_sum


if __name__ == "__main__":
    # Test Cases Basic
    ll = [ListNode().populating([5, 4, 2, 1]), ListNode().populating([4, 2, 2, 3]), ListNode().populating([1, 100000])]

    sols = [6, 7, 100001]

    num_sol = 1
    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, element in enumerate(ll):
            if solution.pairSum(element) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
