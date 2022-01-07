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
#ss = '(){}[]'
#Fateme(ss)

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
    def Fati_Sal_mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # create dummy node so we can compare the first node in each list
        dummy = ListNode()
        # initialise current node pointer
        curr = dummy
        # while the lists are valid
        while list1 and list2:
            # if the value is list1 is less than the value in list2
            if list1.val < list2.val:
                # the next node in the list will be the list1 node
                curr.next = list1
                list1 = list1.next
            else:
                # if not then the next node in the list will be the list2 node
                curr.next = list2
                list2 = list2.next
                # increment node
            curr = curr.next
        # if list1 node is valid but not list2 node add the rest of the nodes from list1
        if list1:
            curr.next = list1

        # if list2 node is valid but not list1 node add the rest of the nodes from list2
        elif list2:
            curr.next = list2

        # return the head of the merged list
        return dummy.next


def mergeTwoLists_mkf(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Runtime: 40 ms, faster than 54.38% of Python3 online submissions for Merge Two Sorted Lists.
    Memory Usage: 14.4 MB, less than 31.72% of Python3 online submissions for Merge Two Sorted Lists.
    """
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    head = list1
    if list2.val <= list1.val:
        head = list2
    cur1 = list1
    cur2 = list2
    cur = None
    prev = None
    while not ((cur1 is None) & (cur2 is None)):
        if cur1 is None:
            prev = cur
            prev.next = cur2
            cur2 = None
        elif cur2 is None:
            prev = cur
            prev.next = cur1
            cur1 = None
        else:
            if cur1.val <= cur2.val:
                node_new = ListNode(cur1.val)
                cur1 = cur1.next
            else:
                node_new = ListNode(cur2.val)
                cur2 = cur2.next

            if cur is None:
                head = node_new
                # prev = node_new
            else:
                prev = cur
                prev.next = node_new
            cur = node_new
    return head


list1 = ListNode(0, ListNode(2, ListNode(4)))
list2 = ListNode(0, ListNode(1, ListNode(3)))
n = mergeTwoLists_mkf(list1, list2)
while n is not None:
    print(n.val)
    n = n.next
print()
