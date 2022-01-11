# *******************************************************
# ************  problem 6  (387 on LeetCode)  *************
# *******************************************************
"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1


Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""

def firstUniqChar_fati(s: str):
    for i, letter in enumerate(s):
        if s.count(letter) == 1:
            return i
    else:
        return -1

print(firstUniqChar_fati("leetcode"))