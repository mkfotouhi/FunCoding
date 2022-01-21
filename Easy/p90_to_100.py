# *******************************************************
# ************  problem 13  (94 on LeetCode)  ***********
# *******************************************************
"""Given the root of a binary tree, return the inorder traversal of its nodes' values."""

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal_mkf(root: Optional[TreeNode]) -> List[int]:
    """
    Runtime: 30 ms, faster than 74.35% of Python3 online submissions for Binary Tree Inorder Traversal.
    Memory Usage: 14.2 MB, less than 48.24% of Python3 online submissions for Binary Tree Inorder Traversal.
    """
    if root is None:
        return []
    if (root.left is None) & (root.right is None):
        return [root.val]
    else:
        return inorderTraversal_mkf(root.left) + [root.val] + inorderTraversal_mkf(root.right)


root = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
print(inorderTraversal_mkf(root))
print()


def inorderTraversal_salamn(root: Optional[TreeNode]) -> List[int]:
    pass


def inorderTraversal_fati(root: Optional[TreeNode]) -> List[int]:
    def rec(root, lst):  # I got some hints to solve it
        if root:
            # First recur on left child
            rec(root.left, lst)

            # then print the data of node
            lst.append(root.val)

            # now recur on right child
            rec(root.right, lst)

    lst = []
    rec(root, lst)
    return lst
