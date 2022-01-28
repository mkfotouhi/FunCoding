# *******************************************************
# ************  problem M1   *************
# *******************************************************
"""
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
from typing import List


def lengthOfLongestSubstring_1(s: str) -> int:
    """
    Runtime: 232 ms, faster than 20.07% of Python3 online submissions for Longest Substring Without Repeating Characters.
    Memory Usage: 14 MB, less than 98.92% of Python3 online submissions for Longest Substring Without Repeating Characters.
    This is an O(n2) Solution which is better than naive O(n3) brute force search approach.
    """

    def last_index(string, start_ind, ch):
        out = 0
        for i, c in enumerate(string):
            if c == ch:
                out = i
        return out + start_ind

    start = 0
    end = 1
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    len_max = 1
    while end < len(s):
        if s[end] in s[start:end]:
            start = last_index(s[start:end], start, s[end]) + 1
        len_max = max(len_max, end - start + 1)
        end = end + 1
    return len_max


print(lengthOfLongestSubstring_1("abcabcbb"))

def lengthOfLongestSubstring_2(s: str) -> int:
    """
    Runtime: 93 ms, faster than 43.29% of Python3 online submissions for Longest Substring Without Repeating Characters.
    Memory Usage: 14 MB, less than 98.91% of Python3 online submissions for Longest Substring Without Repeating Characters.
    This is an O(n) Solution which is better than naive O(n3) and O(n2) brute force search approach.
    """
    start = 0
    end = 1
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    ch_map = {s[0]: 0}
    len_max = 1
    while end < len(s):
        if s[end] in ch_map:
            start = max(start, ch_map[s[end]] + 1)
        ch_map[s[end]] = end
        len_max = max(len_max, end - start + 1)
        end = end + 1
    return len_max

print(lengthOfLongestSubstring_1("abcabcbb"))

# *******************************************************
# ************  problem M2   *************
# *******************************************************
"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
 

Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
Example 2:

Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.
Example 3:

Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
 

Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""


def myAtoi(s: str) -> int:
    """
    Runtime: 51 ms, faster than 37.57% of Python3 online submissions for String to Integer (atoi).
    Memory Usage: 14.1 MB, less than 94.02% of Python3 online submissions for String to Integer (atoi).
    """
    s_new = s
    m = 1
    for ch in s:
        print(ch)
        if ch == ' ':
            s_new = s_new[1:]
            continue
        elif (ch == '-'):
            m = -1
            s_new = s_new[1:]
            break
        elif (ch == '+'):
            s_new = s_new[1:]
            break
        else:
            break
    out = ''
    if len(s_new) == 0:
        return 0
    if not s_new[0].isnumeric():
        return 0
    for ch in s_new:
        if ch.isnumeric():
            out = out + ch
        else:
            break
    ans = m * int(out)
    if ans > 2 ** 31 - 1:
        return 2 ** 31 - 1
    if ans < -2 ** 31:
        return -2 ** 31
    return ans


# *******************************************************
# ************  problem S3   *************
# *******************************************************

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    Runtime: 1347 ms, faster than 7.44% of Python3 online submissions for Move Zeroes.
    Memory Usage: 15.6 MB, less than 17.24% of Python3 online submissions for Move Zeroes.
    """
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.remove(nums[i])
            nums.append(0)

nums = [0, 0, 1, 0, 2, 0, 4, 0, 0]
moveZeroes(nums)
print(nums)