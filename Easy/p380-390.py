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


def firstUniqChar_mkf(s: str) -> int:
    """
    Runtime: 263 ms, faster than 12.23% of Python3 online submissions for First Unique Character in a String.
    Memory Usage: 14.4 MB, less than 70.98% of Python3 online submissions for First Unique Character in a String.
    """
    ind_dict = dict()
    for i, ch in enumerate(s):
        if ch in ind_dict.keys():
            ind_dict[ch] += 1
        else:
            ind_dict[ch] = 1
    for i, ch in enumerate(s):
        if ind_dict[ch] == 1:
            return i
    return -1

print(firstUniqChar_mkf('lee'))
print(firstUniqChar_mkf('leetcode'))
print(firstUniqChar_mkf('loveleetcode'))
print(firstUniqChar_mkf('aabb'))


def firstUniqChar_Salman(s):
    """
    :type s: str
    :rtype: int
    """
    d = {}
    for index, letter in enumerate(s):
        if letter in d.keys():
            d[letter] = -1
        else:
            d[letter] = index
    for i in d.keys():
        if d[i] != -1:
            return d[i]
    return -1