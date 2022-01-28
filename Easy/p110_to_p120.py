# *******************************************************
# ************  problem 9  (111 on LeetCode)  ***********
# *******************************************************
"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5


Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth_mkf(root: Optional[TreeNode]) -> int:
    """
    Runtime: 1015 ms, faster than 5.16% of Python3 online submissions for Minimum Depth of Binary Tree.
    Memory Usage: 53 MB, less than 50.97% of Python3 online submissions for Minimum Depth of Binary Tree.
    """
    if root is None:
        return 0
    if (root.left is None) & (root.right is None):
        return 1
    if (root.left is not None):
        length_l = 1 + minDepth_mkf(root.left)
    else:
        length_l = 0
    if (root.right is not None):
        length_r = 1 + minDepth_mkf(root.right)
    else:
        length_r = 0
    if length_r == 0:
        return length_l
    elif length_l == 0:
        return length_r
    else:
        return min(length_r, length_l)



tree = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))
print(minDepth_mkf(tree))

n1 = TreeNode(15)
n2 = TreeNode(7)
n3 = TreeNode(20, n1, n2)
n4 = TreeNode(9)
n5 = TreeNode(6, n4, n3)
print(minDepth_mkf(n5))


class Solution:
    def minDepth_Salman(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left:
            s_left = 1 + Solution().minDepth_Salman(root.left)
        if root.right:
            s_right = 1 + Solution().minDepth_Salman(root.right)
        if not root.left and not root.right:
            return 1
        if not root.right:
            s_right = s_left
        if not root.left:
            s_left = s_right
        return min(s_left, s_right)

print(Solution().minDepth_Salman(tree))



# *******************************************************
# ************  problem 15  (118 on LeetCode)  ***********
# *******************************************************
"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:



Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
"""

def generate_mkf(numRows: int) -> List[List[int]]:
    out = [[1]]
    for i in range(2, numRows + 1):
        prev = out[i - 2]
        mid = []
        for j in range(len(prev) - 1):
            mid.append(prev[j] + prev[j + 1])

        out.append([1] + mid + [1])
    return out

print(generate_mkf(1))
print(generate_mkf(2))
print(generate_mkf(3))
print(generate_mkf(4))
