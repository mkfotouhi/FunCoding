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


# *******************************************************
# ************  Leetcode 162   *************
# *******************************************************

"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
"""


def findPeakElement(nums: List[int]) -> int:
    if len(nums) == 1:
        return 0
    if len(nums) == 2:
        if nums[0] > nums[1]:
            return 0
        else:
            return 1

    ind_mid = len(nums) // 2
    mid = nums[ind_mid]
    # print(nums)
    # print('ind=', ind_mid, 'mid=', mid)
    if mid > nums[ind_mid - 1]:
        return findPeakElement(nums[ind_mid:len(nums)]) + ind_mid
    else:
        return findPeakElement(nums[0:ind_mid])

print(findPeakElement([1, 2, 3, 2, 4]))

def findPeakElement_iterative(nums: List[int]) -> int:
    ind = 0
    while len(nums) > 2:
        ind_mid = len(nums) // 2
        mid = nums[ind_mid]
        # print(nums)
        # print('ind=', ind_mid, 'mid=', mid)
        if mid > nums[ind_mid - 1]:
            nums = nums[ind_mid:len(nums)]
            ind = ind + ind_mid
        else:
            nums = nums[0:ind_mid]
    if len(nums) == 1:
        return ind
    if nums[0] > nums[1]:
        return ind
    else:
        return ind + 1

print(findPeakElement_iterative([1, 2, 3, 2, 4]))