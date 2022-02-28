"""
Reverse Operations
You are given a singly-linked list that contains N integers. A subpart of the list is a contiguous set of even elements, bordered either by either end of the list or an odd element. For example, if the list is [1, 2, 8, 9, 12, 16], the subparts of the list are [2, 8] and [12, 16].
Then, for each subpart, the order of the elements is reversed. In the example, this would result in the new list, [1, 8, 2, 9, 16, 12].
The goal of this question is: given a resulting list, determine the original order of the elements.
Implementation detail:
You must use the following definition for elements in the linked list:
class Node {
    int data;
    Node next;
}
Signature
Node reverse(Node head)
Constraints
1 <= N <= 1000, where N is the size of the list
1 <= Li <= 10^9, where Li is the ith element of the list
Example
Input:
N = 6
list = [1, 2, 8, 9, 12, 16]
Output:
[1, 8, 2, 9, 16, 12]
"""


# Add any extra import statements you may need here


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


# Add any helper functions you may need here


def reverse(head):
    # Write your code here
    cur = head
    out = []
    temp_even = []
    i = 0
    new_head = Node(head.data)
    while (cur is not None):
        if cur.data % 2 == 0:
            temp_even.append(cur.data)
        else:
            temp_even.reverse()
            out = out + temp_even
            out.append(cur.data)
            temp_even = []

        cur = cur.next
        i += 1
    temp_even.reverse()
    out = out + temp_even

    return createLinkedList(out)


def createLinkedList(arr):
    head = None
    tempHead = head
    for v in arr:
        if head == None:
            head = Node(v)
            tempHead = head
        else:
            head.next = Node(v)
            head = head.next
    return tempHead

head_1 = createLinkedList([1, 2, 8, 9, 12, 16])
print(reverse(head_1))