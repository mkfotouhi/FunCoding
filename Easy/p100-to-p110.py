# *******************************************************
# ************  problem 7  (100 on LeetCode)  *************
# *******************************************************
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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

p = TreeNode(1)
p_left = TreeNode(2)
p.left = p_left

q = TreeNode(1)
q_left = TreeNode(1)
q.left = q_left

def isSameTree_Fati(p, q) -> bool:
    flag = True
    if p and q and p.val == q.val:
        flag = isSameTree_Fati(p.left, q.left)
        if flag:
            flag = isSameTree_Fati(p.right, q.right)
    elif ((not q) and p) or ((not p) and q):
        flag = False
    elif p and q and p.val != q.val:
        flag = False
    return flag
print(isSameTree_Fati(p,q))