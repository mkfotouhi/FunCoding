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


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    n1 = list1
    n2 = list2
    n1_val = list1.val
    n2_val = list2.val
    out = ListNode()

    while not ((n1_val is None) & (n2_val is None)):
        if n2_val is None:
            out.val = n1_val
            n1 = n1.next
        elif n1_val is None:
            out.val = n2_val
            n2 = n2.next
        elif n1_val <= n2_val:
            out.val = n1_val
            n1 = n1.next
        elif n2_val <= n1_val:
            out.val = n2_val
            n2 = n2.next
        out.next = ListNode()
        out = out.next
        if n1 is None:
            n1_val = None
        else:
            n1_val = n1.val
        if n2 is None:
            n2_val = None
        else:
            n2_val = n2.val

    return out
list1 = ListNode(0, ListNode(2, ListNode(4)))
list2 = ListNode(0, ListNode(1, ListNode(3)))
n = mergeTwoLists(list1, list2)
while n is not None:
    print(n.val)
    n=n.next
print()