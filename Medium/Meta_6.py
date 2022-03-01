"""
Slow Sums
Suppose we have a list of N numbers, and repeat the following operation until we're left with only a single number: Choose any two numbers and replace them with their sum. Moreover, we associate a penalty with each operation equal to the value of the new number, and call the penalty for the entire list as the sum of the penalties of each operation.
For example, given the list [1, 2, 3, 4, 5], we could choose 2 and 3 for the first operation, which would transform the list into [1, 5, 4, 5] and incur a penalty of 5. The goal in this problem is to find the highest possible penalty for a given input.
Signature:
int getTotalTime(int[] arr)
Input:
An array arr containing N integers, denoting the numbers in the list.
Output format:
An int representing the highest possible total penalty.
Constraints:
1 ≤ N ≤ 10^6
1 ≤ Ai ≤ 10^7, where *Ai denotes the ith initial element of an array.
The sum of values of N over all test cases will not exceed 5 * 10^6.
Example
arr = [4, 2, 1, 3]
output = 26
First, add 4 + 3 for a penalty of 7. Now the array is [7, 2, 1]
Add 7 + 2 for a penalty of 9. Now the array is [9, 1]
Add 9 + 1 for a penalty of 10. The penalties sum to 26.
"""


def getTotalTime(arr):
    # Write your code here
    arr.sort(reverse=True)
    print(arr)
    new_num = arr[0]
    out = 0
    for i in range(1, len(arr)):
        print(f'out:{out}, new_num={new_num}')
        new_num += arr[i]
        out += new_num
    return out


print(getTotalTime([4, 2, 1, 3]))
print(getTotalTime([2, 3, 9, 8, 4]))

"""
Element Swapping
Given a sequence of n integers arr, determine the lexicographically smallest sequence which may be obtained from it after performing at most k element swaps, each involving a pair of consecutive elements in the sequence.
Note: A list x is lexicographically smaller than a different equal-length list y if and only if, for the earliest index at which the two lists differ, x's element at that index is smaller than y's element at that index.
Signature
int[] findMinArray(int[] arr, int k)
Input
n is in the range [1, 1000].
Each element of arr is in the range [1, 1,000,000].
k is in the range [1, 1000].
Output
Return an array of n integers output, the lexicographically smallest sequence achievable after at most k swaps.
Example 1
n = 3
k = 2
arr = [5, 3, 1]
output = [1, 5, 3]
We can swap the 2nd and 3rd elements, followed by the 1st and 2nd elements, to end up with the sequence [1, 5, 3]. This is the lexicographically smallest sequence achievable after at most 2 swaps.
Example 2
n = 5
k = 3
arr = [8, 9, 11, 2, 1]
output = [2, 8, 9, 11, 1]
We can swap [11, 2], followed by [9, 2], then [8, 2].
"""


def minimizeWithKSwaps(arr, k):
    n = len(arr)
    for i in range(n - 1):

        # Set the position where we we want
        # to put the smallest integer
        pos = i
        for j in range(i + 1, n):

            # If we exceed the Max swaps
            # then terminate the loop
            if (j - i > k):
                break

            # Find the minimum value from i+1 to
            # max (k or n)
            if (arr[j] < arr[pos]):
                pos = j

        # Swap the elements from Minimum position
        # we found till now to the i index
        for j in range(pos, i, -1):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]

        # Set the final value after swapping pos-i
        # elements
        k -= pos - i
    return arr


print(minimizeWithKSwaps([8, 9, 11, 2, 1], 3))

"""
Seating Arrangements
There are n guests attending a dinner party, numbered from 1 to n. The ith guest has a height of arr[i-1] inches.
The guests will sit down at a circular table which has n seats, numbered from 1 to n in clockwise order around the table. As the host, you will choose how to arrange the guests, one per seat. Note that there are n! possible permutations of seat assignments.
Once the guests have sat down, the awkwardness between a pair of guests sitting in adjacent seats is defined as the absolute difference between their two heights. Note that, because the table is circular, seats 1 and n are considered to be adjacent to one another, and that there are therefore n pairs of adjacent guests.
The overall awkwardness of the seating arrangement is then defined as the maximum awkwardness of any pair of adjacent guests. Determine the minimum possible overall awkwardness of any seating arrangement.
Signature
int minOverallAwkwardness(int[] arr)
Input
n is in the range [3, 1000].
Each height arr[i] is in the range [1, 1000].
Output
Return the minimum achievable overall awkwardness of any seating arrangement.
Example
n = 4
arr = [5, 10, 6, 8]
output = 4
If the guests sit down in the permutation [3, 1, 4, 2] in clockwise order around the table (having heights [6, 5, 8, 10], in that order), then the four awkwardnesses between pairs of adjacent guests will be |6-5| = 1, |5-8| = 3, |8-10| = 2, and |10-6| = 4, yielding an overall awkwardness of 4. It's impossible to achieve a smaller overall awkwardness.

"""


def minOverallAwkwardness(arr):
    # Write your code here
    arr.sort()
    min_val = 0
    for i in range(len(arr) - 2):
        min_val = max(abs(arr[i] - arr[i + 2]), min_val)
    min_val = max(abs(arr[0] - arr[1]), min_val)
    min_val = max(abs(arr[-1] - arr[-2]), min_val)
    return min_val

print(minOverallAwkwardness([5, 10, 6, 8]))


