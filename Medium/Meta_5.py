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


def numberOfWays_2(arr, k):
    # Write your code here
    val_dict = dict()
    for i in range(len(arr)):
        num = arr[i]
        val_dict[num] = val_dict.get(num, 0) + 1

    count = 0
    for i in range(len(arr)):
        rem = k - arr[i]
        if rem in val_dict.keys():
            if rem == k // 2:
                count += val_dict[rem] - 1
            else:
                count += val_dict[rem]
    return int(count / 2)


print(numberOfWays_2([1, 5, 3, 3, 3], 6))

"""
Number of Visible Nodes
There is a binary tree with N nodes. You are viewing the tree from its left side and can see only the leftmost nodes at each level. Return the number of visible nodes.
Note: You can see only the leftmost nodes, but that doesn't mean they have to be left nodes. The leftmost node at a level could be a right node.
Signature
int visibleNodes(Node root) {
Input
The root node of a tree, where the number of nodes is between 1 and 1000, and the value of each node is between 0 and 1,000,000,000
Output
An int representing the number of visible nodes.
Example
            8  <------ root
           / \
         3    10
        / \     \
       1   6     14
          / \    /
         4   7  13            
output = 4
"""


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def visible_nodes(root):
    # Write your code here
    if (root.left is not None) and (root.right is not None):
        return 1 + max(visible_nodes(root.left), visible_nodes(root.right))
    elif root.left is not None:
        return 1 + visible_nodes(root.left)
    elif root.right is not None:
        return 1 + visible_nodes(root.right)
    else:
        return 1


root_2 = TreeNode(10)
root_2.left = TreeNode(8)
root_2.right = TreeNode(15)
root_2.left.left = TreeNode(4)
root_2.left.left.right = TreeNode(5)
root_2.left.left.right.right = TreeNode(6)
root_2.right.left = TreeNode(14)
root_2.right.right = TreeNode(16)

print('visible nodes:', visible_nodes(root_2))

"""
Nodes in a Subtree
You are given a tree that contains N nodes, each containing an integer u which corresponds to a lowercase character c in the string s using 1-based indexing.
You are required to answer Q queries of type [u, c], where u is an integer and c is a lowercase letter. The query result is the number of nodes in the subtree of node u containing c.
Signature
int[] countOfNodes(Node root, ArrayList<Query> queries, String s)
Input
A pointer to the root node, an array list containing Q queries of type [u, c], and a string s
Constraints
N and Q are the integers between 1 and 1,000,000
u is a unique integer between 1 and N
s is of the length of N, containing only lowercase letters
c is a lowercase letter contained in string s
Node 1 is the root of the tree
Output
An integer array containing the response to each query
Example
        1(a)
        /   \
      2(b)  3(a)
s = "aba"
RootNode = 1
query = [[1, 'a']]
Note: Node 1 corresponds to first letter 'a', Node 2 corresponds to second letter of the string 'b', Node 3 corresponds to third letter of the string 'a'.
output = [2]
Both Node 1 and Node 3 contain 'a', so the number of nodes within the subtree of Node 1 containing 'a' is 2.
"""


class Node_m:
    def __init__(self, data):
        self.val = data
        self.children = []


# Add any helper functions you may need here
def count_subtree(node: Node_m, s, ch):
    if node is None:
        return 0
    else:
        total = 0
        for child in node.children:
            total = total + count_subtree(child, s, ch)
        if s[node.val - 1] == ch:
            return 1 + total
        else:
            return total

def find_node(root: Node_m, q_int):
    node_queue = [root]
    while len(node_queue) > 0:
        node = node_queue.pop(0)
        if node.val == q_int:
            return node
        else:
            for child in node.children:
                if child not in node_queue:
                    node_queue.append(child)
    return None
    # print(f'starting on:{root.val}')
    # if root.val == q_int:
    #     print('   found the node:', root.val)
    #     return root
    # # elif len(root.children) > 0:
    # for child in root.children:
    #     print(f'   root:{root.val}, n_children:{len(root.children)}, child:{child.val}')
    #     return find_node(child, q_int)
    # return


def count_of_nodes(root, queries, s):
    # Write your code here
    out = []
    dict_q = dict()
    for i in range(len(queries)):
        q = queries[i]
        dict_q[q[0]] = q[1]
    for q in queries:
        print('-'*50)
        print('q_int=', q[0])
        node = find_node(root, q[0])

        if node is None:
            out.append(0)
            print(f'q:{q}, node:{node}')
        else:
            child_vals = []
            for child in node.children:
                child_vals.append(child.val)
            out.append(count_subtree(node, s, q[1]))
            print(f'q:{q}, node:{node.val}, children: {child_vals}', )
    return out


# Testcase 2
# print(find_node(Node_m(4), 4))
n_2, q_2 = 7, 3
s_2 = "abaacab"
root_2 = Node_m(1)
root_2.children.append(Node_m(2))
root_2.children.append(Node_m(3))
root_2.children.append(Node_m(7))
root_2.children[0].children.append(Node_m(4))
root_2.children[0].children.append(Node_m(5))
root_2.children[1].children.append(Node_m(6))
queries_2 = [(1, 'a'), (2, 'b'), (3, 'a')]
print('count_of_nodes:', count_of_nodes(root_2, queries_2, s_2))
