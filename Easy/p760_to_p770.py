# *******************************************************
# ************  problem 14  (766 on LeetCode)  *************
# *******************************************************
"""
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Example 1:

Input: matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

Example 2:

Input: matrix = [[1, 2], [2, 2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99"""
from typing import List


def isToeplitzMatrix_mkf(matrix: List[List[int]]) -> bool:
    """
    Runtime: 117 ms, faster than 32.24% of Python3 online submissions for Toeplitz Matrix.
    Memory Usage: 14.4 MB, less than 36.35% of Python3 online submissions for Toeplitz Matrix.
    """
    w = len(matrix[0])
    h = len(matrix)
    i = 0
    flag = True
    for i in range(w - 1):
        for j in range(h - 1):
            if not (matrix[j][i] == matrix[j + 1] [i + 1]):
                flag = False
    return flag


matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print(isToeplitzMatrix_mkf(matrix))