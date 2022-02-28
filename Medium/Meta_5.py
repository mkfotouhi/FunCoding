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

"""
Pair Sums
Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.
If an integer appears in the list multiple times, each copy is considered to be different; that is, two pairs are considered different if one pair includes at least one array index which the other doesn't, even if they include the same values.
Signature
int numberOfWays(int[] arr, int k)
Input
n is in the range [1, 100,000].
Each value arr[i] is in the range [1, 1,000,000,000].
k is in the range [1, 1,000,000,000].
Output
Return the number of different pairs of elements which sum to k.
Example 1
n = 5
k = 6
arr = [1, 2, 3, 4, 3]
output = 2
The valid pairs are 2+4 and 3+3.
Example 2
n = 5
k = 6
arr = [1, 5, 3, 3, 3]
output = 4
There's one valid pair 1+5, and three different valid pairs 3+3 (the 3rd and 4th elements, 3rd and 5th elements, and 4th and 5th elements).
"""


def numberOfWays(arr, k):
    # Write your code here
    val_dict = dict()
    for i in range(len(arr)):
        num = arr[i]
        if num in val_dict.keys():
            val_dict[num].append(i)
        else:
            val_dict[num] = [i]

    count = 0
    for i in range(len(arr)):
        rem = k - arr[i]
        if rem in val_dict.keys():
            inds = val_dict[rem]
            for j in range(len(inds)):
                if inds[j] > i:
                    count += 1
    return count


print(numberOfWays([1, 5, 3, 3, 3], 6))
