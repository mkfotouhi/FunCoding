# *******************************************************
# ************  problem 1  (9 on LeetCode)  *************
# *******************************************************
"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-2^31 <= x <= 2^31 - 1

"""


def isPalindrome(x: int) -> bool:
    return True

def Fateme(x: int) -> bool: #return true if x is palindrome integer.
    if -2**31 <= x and x <= (2**31 -1):
        x_str = str(x)
        if len(x_str) == 1:
            return True
        for i in range(int(len(x_str)/2)):
            if x_str[i] != x_str[-i-1]:
                return False
        return True
    else:
        return False

Fateme(1000021)