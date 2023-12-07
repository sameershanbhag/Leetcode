# Author: Sameer Shanbhag
# Leetcode Problem:
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
# Medium

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other):
        if not other:
            return False
        return self.val == other.val


def generate_tree(input_array: List[int]):
    if not input_array:
        return None
    root = TreeNode(input_array[0])
    queue = [root]
    i = 1
    while i < len(input_array):
        current = queue.pop(0)
        if input_array[i] is not None:
            current.left = TreeNode(input_array[i])
            queue.append(current.left)
        i += 1
        if input_array[i] is not None:
            current.right = TreeNode(input_array[i])
            queue.append(current.right)
        i += 1
    return root


class Solution0:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right


if __name__ == '__main__':
    # Test Cases Basic
    tree_nodes = [[generate_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), TreeNode(5), TreeNode(1)],
                  [generate_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), TreeNode(5), TreeNode(4)]]

    sols = [TreeNode(3), TreeNode(5)]

    num_sol = 1

    for i in range(num_sol):
        solution = eval(f"Solution{i}()")
        for j, current in enumerate(tree_nodes):
            ans = solution.lowestCommonAncestor(current[0], current[1], current[2])
            if ans == sols[j]:
                print("PASS")
            else:
                print("FAIL")
