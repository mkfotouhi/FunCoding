# *******************************************************
# ************  problem 5  (206 on LeetCode)  *************
# *******************************************************
"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example
1:

Input: head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
Example
2:

Input: head = [1, 2]
Output: [2, 1]
Example
3:

Input: head = []
Output: []

Constraints:

The
number
of
nodes in the
list is the
range[0, 5000].
-5000 <= Node.val <= 5000"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#    pass


### example

list_rev = ListNode(1)
second = ListNode(2)
third = ListNode(3)
list_rev.next = second
second.next = third


def reverseList_fati(head):
    if head:
        rev_list = ListNode(head.val)
        head = head.next
        while head:
            head_rev = ListNode(head.val)
            head_rev.next = rev_list
            rev_list = head_rev
            head = head.next
    else:
        rev_list = head
    return rev_list


print(reverseList_fati(list_rev).val)
