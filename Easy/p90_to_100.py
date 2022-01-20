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
    pass


def inorderTraversal_salamn(root: Optional[TreeNode]) -> List[int]:
    pass


def inorderTraversal_fati(root: Optional[TreeNode]) -> List[int]:
    def rec(root, lst): #I got some hints to solve it
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
