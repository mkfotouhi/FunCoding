# *******************************************************
# ************  problem 3  (20 on LeetCode)  *************
# *******************************************************
"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'."""


def isValid_mkf(s: str) -> bool:
    open_lst = ['(', '[', '{']
    close_lst = [')', ']', '}']
    stack = []
    flag = True
    for ch in s:
        if ch in open_lst:
            stack.append(ch)
        else:
            if len(stack) > 0:
                if open_lst[close_lst.index(ch)] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    flag = False
            else:
                flag = False
    if len(stack) > 0:
        flag = False

    return flag


assert (isValid_mkf('{[()]}') is True)
assert (isValid_mkf('{[()]') is False)
