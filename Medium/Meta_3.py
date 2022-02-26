# *******************************************************
# ************  Leetcode 125   *************
# *******************************************************
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
from typing import List


def isPalindrome(s: str) -> bool:
    alpha_list = [x.lower() for x in s if x.isalnum()]
    backward = [alpha_list[i] for i in reversed(range(len(alpha_list)))]
    for i in range(len(alpha_list)):
        if alpha_list[i] != backward[i]:
            return False
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))

# *******************************************************
# ************  Leetcode 50   *************
# *******************************************************
"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104"""


def fastPow(x, n):
    if n == 0:
        return 1
    half = fastPow(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x


def myPow(x: float, n: int) -> float:
    if n < 0:
        n = -n
        x = 1 / x
    return fastPow(x, n)


print(myPow(2, 10), myPow(2, -4))


def myPow_iterative(x, n):
    if n < 0:
        n = -n
        x = 1 / x
    if n == 0:
        return 1
    steps = []
    p = n
    while p > 0:
        steps.append(p)
        p = p // 2

    steps.reverse()
    val = 1
    for step in steps:
        if step % 2 == 1:
            val = val * val * x
        else:
            val = val * val
    return val

# *******************************************************
# ************  Leetcode 56   *************
# *******************************************************
"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals = sorted(intervals)
    # print(intervals)
    out = [intervals[0]]
    for i in range(1, len(intervals)):
        new = intervals[i]
        cur = out[-1]
        if cur[1] >= new[0]:  # ovrlap
            out[-1] = [min(cur[0], new[0]), max(cur[1], new[1])]
        else:
            out.append(new)
    return out

print(merge([[1,3],[2,6],[8,10],[15,18]]))