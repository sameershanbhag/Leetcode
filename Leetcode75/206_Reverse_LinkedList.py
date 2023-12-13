# Author: Sameer Shanbhag
# Leetcode Problem:
# https://leetcode.com/problems/reverse-linked-list
# Easy
from typing import Optional

from ListNode import ListNode


class Solution0:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            new_node = current.next
            current.next = previous
            previous = current
            current = new_node

        return previous


if __name__ == "__main__":
    # Test Cases Basic
    ll = [ListNode().populating([1, 2, 3, 4, 5]), ListNode().populating([1, 2]), None]

    sols = [ListNode().populating([5, 4, 3, 2, 1]), ListNode().populating([2, 1]), None]

    num_sol = 1
    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, element in enumerate(ll):
            if solution.reverseList(element) == sols[j]:
                print("PASS")
            else:
                print("FAIL")
