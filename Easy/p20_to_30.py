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

class Solution(object):
    def fati_sal(self, s):

        dic_item = {"(": ")", "[": "]", "{": "}"}
        pair = []
        for item in s:
            if item in dic_item.keys():
                pair.append(dic_item[item])
            else:
                if not pair:
                    return False
                elif item == pair[-1]:
                    pair.pop()
                else:
                    return False
        return not pair

obj = Solution()
print(obj.fati_sal("(])"))