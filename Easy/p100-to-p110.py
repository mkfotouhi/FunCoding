"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example
1:

Input: p = [1, 2, 3], q = [1, 2, 3]
Output: true
Example
2:

Input: p = [1, 2], q = [1, null, 2]
Output: false
Example
3:

Input: p = [1, 2, 1], q = [1, 1, 2]
Output: false

Constraints:

The
number
of
nodes in both
trees is in the
range[0, 100].
-104 <= Node.val <= 104 """

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isSameTree_mkf(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Runtime: 39 ms, faster than 27.01% of Python3 online submissions for Same Tree.
    Memory Usage: 14.2 MB, less than 86.07% of Python3 online submissions for Same Tree.
    """
    if not p and not q:
        return True
    # one of p and q is None
    if not q or not p:
        return False
    if p.val != q.val:
        return False
    return isSameTree_mkf(p.right, q.right) and isSameTree_mkf(p.left, q.left)





