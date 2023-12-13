# Author: Sameer Shanbhag
# Leetcode Problem:
# https://leetcode.com/problems/odd-even-linked-list
# Medium
from typing import Optional

from ListNode import ListNode


class Solution0:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head

        evenHead = even = head.next

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = evenHead

        return head


if __name__ == "__main__":
    # Test Cases Basic
    ll = [ListNode().populating([1, 2, 3, 4, 5]), ListNode().populating([2, 1, 3, 5, 6, 4, 7]),
          ListNode().populating([1, 2, 3, 4, 5, 6, 7, 8])]

    sols = [ListNode().populating([1, 3, 5, 2, 4]), ListNode().populating([2, 3, 6, 7, 1, 5, 4]),
            ListNode().populating([1, 3, 5, 7, 2, 4, 6, 8])]

    num_sol = 1
    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, element in enumerate(ll):
            solution.oddEvenList(element)
            if element == sols[j]:
                print("PASS")
            else:
                print("FAIL")
