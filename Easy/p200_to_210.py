# *******************************************************
# ************  problem 11 (202 on LeetCode)  *************
# *******************************************************
"""
Happy Number :)

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:

Input: n = 2
Output: false

Constraints:

1 <= n <= 2^31 - 1"""

def isHappy_mkf(n: int) -> bool:
    """
    Runtime: 35 ms, faster than 71.13% of Python3 online submissions for Happy Number.
    Memory Usage: 14.3 MB, less than 48.95% of Python3 online submissions for Happy Number.
    """
    def next_number(n_):
        out = 0
        for ch in str(n_):
            out += int(ch)**2
        return out

    visited_num = set()
    cur = n
    while cur not in visited_num:
        visited_num.add(cur)
        cur = next_number(cur)
        if cur == 1:
            return True
    return False

print(isHappy_mkf(100))
print(isHappy_mkf(2))
print(isHappy_mkf(19))
print(isHappy_mkf(99))

def isHappy_fati(n) -> bool:

    prev = set()
    while n != 1:
        n = sum(list(map(lambda x: pow(int(x), 2), list(str(n)))))
        if n in prev:
            return False
        prev.add(n)
    else:
        return True
print(isHappy_fati(19))


def isHappy_Salman(n: int) -> bool:
    happy_list = []
    while (True):
        x = [int(i) for i in str(n)]
        xx = sum(i * i for i in x)
        if xx == 1:
            return True
        elif xx in happy_list:
            return False
        else:
            happy_list.append(xx)
            n = xx

print(isHappy_Salman(100))
print(isHappy_Salman(2))

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


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution_Salman(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reverse = ListNode(head.val) if head else head

        while head:
            head = head.next
            if head:
                current = ListNode(head.val, reverse)
                reverse = current

        return reverse

list1 = ListNode(0, ListNode(2, ListNode(4)))

Solution_Salman().reverseList(list1)


### example

list_rev = ListNode(1)
second = ListNode(2)
third = ListNode(3)
list_rev.next = second
second.next = third

def reverseList_mkf(head):
    """
    Runtime: 32 ms, faster than 89.01% of Python3 online submissions for Reverse Linked List.
    Memory Usage: 16.5 MB, less than 20.89% of Python3 online submissions for Reverse Linked List.
    """
    if head:
        if head.next:
            cur = head
            next_cur = cur.next
            out = ListNode(head.val)
            while next_cur is not None:
                cur = next_cur
                out = ListNode(cur.val, out)
                next_cur = cur.next
            return out
        else:
            return head
    else:
        return head


print(reverseList_mkf(list_rev).val)
print(reverseList_mkf(ListNode(0)).val)



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

