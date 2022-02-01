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
from typing import List


def isPalindrome_mkf(x: int) -> bool:
    '''
    Runtime: 56 ms, faster than 81.44% of Python3 online submissions for Palindrome Number.
    Memory Usage: 14.3 MB, less than 15.65% of Python3 online submissions for Palindrome Number.
    '''
    s = str(x)
    flag = True
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            flag = False
    return flag


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

def isPalindrome_Salman(x: int) -> bool:
    """
    :type x: int
    :rtype: bool
    """
    x_str = str(x)
    len_str = len(x_str)
    if len_str == 1:
        return True
    elif x_str[0: len_str//2: 1] == x_str[len_str-1:len_str-1-len_str//2:-1]:
        return True
    else:
        return False


# *******************************************************
# ************  problem 17  (1 on LeetCode)  *************
# *******************************************************
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Runtime: 86 ms, faster than 57.89% of Python3 online submissions for Two Sum.
    Memory Usage: 15.3 MB, less than 55.73% of Python3 online submissions for Two Sum.
    This solution is an O(n) in time complexity and space.
    """
    comp_dict = dict()
    for i, num in enumerate(nums):
        if (target - num) in comp_dict:
            return [i, comp_dict[target - num]]
        else:
            comp_dict[num] = i
    return []


print(twoSum(nums=[3, 2, 4], target=6))  # [1, 2]