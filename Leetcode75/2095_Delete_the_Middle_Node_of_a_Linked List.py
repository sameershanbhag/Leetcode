# Author: Sameer Shanbhag
# Leetcode Problem:
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list
# Medium
from typing import Optional

from ListNode import ListNode


class Solution0:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return

        dummy = ListNode()
        dummy.next = head
        current = head
        fast = head.next.next

        while fast and fast.next:
            current = current.next
            fast = fast.next.next

        current.next = current.next.next

        return dummy.next


if __name__ == "__main__":
    # Test Cases Basic
    ll = [ListNode().populating([1, 3, 4, 7, 1, 2, 6]), ListNode().populating([1, 2, 3, 4]),
                   ListNode().populating([1, 2, 3, 4, 5]), ListNode().populating([1, 2, 3, 4, 5, 6])]

    sols = [ListNode().populating([1, 3, 4, 1, 2, 6]), ListNode().populating([1, 2, 4]),
            ListNode().populating([1, 2, 4, 5]), ListNode().populating([1, 2, 3, 5, 6])]

    num_sol = 1
    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, element in enumerate(ll):
            solution.deleteMiddle(element)
            if element == sols[j]:
                print("PASS")
            else:
                print("FAIL")
