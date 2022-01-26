# *******************************************************
# ************  problem 15  (53 on LeetCode)  *************
# *******************************************************
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
from typing import List


def maxSubArray_mkf(nums: List[int]) -> int:
    """
    Runtime: 768 ms, faster than 63.73% of Python3 online submissions for Maximum Subarray.
    Memory Usage: 28.8 MB, less than 33.71% of Python3 online submissions for Maximum Subarray.
    """
    out = nums[0]
    prev = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        prev = max(num, prev + num)
        out = max(out, prev)
    return out


print(maxSubArray_mkf([-1, 2, 1, -1, 4, -8, 10]))
print(maxSubArray_mkf([1, 2, 3, 4]))
print(maxSubArray_mkf([-1, -2, -3, 5, -4, 5, -10]))
print(maxSubArray_mkf([1]))
print(maxSubArray_mkf([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(maxSubArray_mkf([4, -1, 2, 1]))  # 6
print(maxSubArray_mkf([5, 4, -1, 7, 8]))  # 23
print(maxSubArray_mkf([-1, -2]))  # 23


def maxSubArray_fati(nums: List[int]) -> int:
    pass


def maxSubArray_Salman(nums: List[int]) -> int:
    pass
