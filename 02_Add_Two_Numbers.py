# Author: Sameer Shanbhag
# Leetcode Problem: https://leetcode.com/problems/add-two-numbers/
# Medium

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {str(self.next)}"

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.val == other.val and self.next == other.next


class Solution0:
    def generate_from_list(self, node_list: List):
        current_node = None
        return_node = None

        for current_element in node_list:
            if current_node is None:
                current_node = ListNode(current_element)
                return_node = current_node
            else:
                current_node.next = ListNode(current_element)
                current_node = current_node.next

        return return_node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Input Validation
        if l1 is None:
            return

        if l2 is None:
            return

        addition = [0, 0]
        itr = 0
        while l1 is not None or l2 is not None:
            if l1 is not None:
                addition[0] = 10 ** itr * l1.val + addition[0]
                l1 = l1.next

            if l2 is not None:
                addition[1] = 10 ** itr * l2.val + addition[1]
                l2 = l2.next

            itr += 1

        output = addition[1] + addition[0]
        output = [int(x) for x in reversed(str(output))]
        return self.generate_from_list(output)


class Solution1:
    def generate_from_list(self, node_list: List):
        current_node = None
        return_node = None

        for current_element in node_list:
            if current_node is None:
                current_node = ListNode(current_element)
                return_node = current_node
            else:
                current_node.next = ListNode(current_element)
                current_node = current_node.next

        return return_node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        final_listnode = ListNode()
        append_listnode = final_listnode

        carry = 0

        # Input Validation
        if l1 is None:
            return

        if l2 is None:
            return

        while l1 is not None or l2 is not None:
            num1, num2 = 0, 0
            if l1 is not None:
                num1 = l1.val
                l1 = l1.next

            if l2 is not None:
                num2 = l2.val
                l2 = l2.next

            current_add = num1 + num2 + carry

            if current_add >= 10:
                carry = 1
                current_add -= 10
            else:
                carry = 0
            append_listnode.next = ListNode(current_add)
            append_listnode = append_listnode.next

        if carry == 1:
            append_listnode.next = ListNode(carry)

        return final_listnode.next


if __name__ == '__main__':
    # Test Cases Basic
    nums = [[[2, 4, 3], [5, 6, 4]], [[0], [0]], [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]]]

    sols = [[7, 0, 8], [0], [8, 9, 9, 9, 0, 0, 0, 1]]

    num_sol = 2

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(nums):
            current_sol = solution.addTwoNumbers(solution.generate_from_list(current[0]),
                                                 solution.generate_from_list(current[1]))
            if current_sol == solution.generate_from_list(sols[j]):
                print("PASS")
            else:
                print("FAIL")
