# *******************************************************
# ************  problem 19  (67 on LeetCode)  *************
# *******************************************************

"""
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""

def addBinary_mkf(a: str, b: str) -> str:
    """
    Runtime: 44 ms, faster than 50.73% of Python3 online submissions for Add Binary.
    Memory Usage: 14 MB, less than 97.33% of Python3 online submissions for Add Binary.
    Time complexity: O(n), space: O(n)
    """
    num1 = a[::-1]
    num2 = b[::-1]
    total = ''
    over = 0
    for i in range(max(len(a), len(b))):
        print()
        if i < len(a):
            s1 = int(num1[i])
        else:
            s1 = 0
        if i < len(b):
            s2 = int(num2[i])
        else:
            s2 = 0
        if s1 + s2 + over < 2:
            total = str(s1 + s2 + over) + total
            over = 0
        else:
            total = str(s1 + s2 + over - 2) + total
            over = 1
    if over == 1:
        total = '1' + total
    return total