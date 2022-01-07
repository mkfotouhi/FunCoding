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
from typing import Optional


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


def Fateme(s):
    """
    :type s: str
    :rtype: bool
    """

    stack = []

    # Traversing the Expression
    for char in s:
        if char in ["(", "{", "["]:

            # Push the element in the stack
            stack.append(char)
        else:

            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    return not stack
ss = '(){}[]'
Fateme(ss)

# *******************************************************
# ************  problem 4  (21 on LeetCode)  *************
# *******************************************************
"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order."""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):

        final_list_o = ListNode()
        final_list = final_list_o

        while list1 or list2:
            if list1 and list2 and list1.val <= list2.val:
                final_list.next = ListNode(list1.val)
                final_list = final_list.next
                list1 = list1.next
            elif list1 and list2 and list1.val > list2.val:
                final_list.next = ListNode(list2.val)
                final_list = final_list.next
                list2 = list2.next
            elif list1 and not list2:
                final_list.next = ListNode(list1.val)
                final_list = final_list.next
                list1 = list1.next
            else:
                final_list.next = ListNode(list2.val)
                final_list = final_list.next
                list2 = list2.next

        return final_list_o.next

list1_1 = ListNode(1)
list1_2 = ListNode(2)
list1_3 = ListNode(4)
list1_1.next = list1_2
list1_2.next = list1_3

list2_1 = ListNode(1)
list2_2 = ListNode(3)
list2_3 = ListNode(4)
list2_1.next = list2_2
list2_2.next = list2_3

# temp = list1_1
# while temp:
#   print(temp.val)
#   temp = temp.next
Solution().mergeTwoLists(list1_1, list2_1)