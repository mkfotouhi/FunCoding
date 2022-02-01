# *******************************************************
# ************  Leetcode 26   *************
# *******************************************************

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.



Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:

0 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""
from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    num = nums[0]
    i = 0
    while num != '_':
        j = i + 1
        while (j < len(nums)) and (nums[j] == num):
            nums.remove(num)
            nums.append('_')
        i += 1
        if i < len(nums):
            num = nums[i]
        else:
            break
    return i


def removeDuplicates_faster(nums: List[int]) -> int:
    if len(nums) < 2:
        return len(nums)
    real_ind = 0
    for i in range(len(nums)):
        if nums[i] != nums[real_ind]:
            real_ind += 1
        nums[real_ind] = nums[i]
    return real_ind + 1

print(removeDuplicates_faster([1, 1, 2]))
print(removeDuplicates_faster([0,0,1,1,1,2,2,3,3,4]))


# *******************************************************
# ************  Leetcode 76   *************
# *******************************************************

"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters."""


def minWindow_1(s: str, t: str) -> str:
    def l2_in_l1(list1, list2):
        for n in list2:
            if list1.count(n) < list2.count(n):
                return False
        return True

    min_len = max(len(s), len(t)) + 1
    p1 = 0
    p2 = 1

    ind_list = []
    main_ch = []
    len_dict = dict()
    for i, ch in enumerate(s):
        if (ch in t):
            main_ch.append(ch)
            ind_list.append(i)
    for i in range(len(main_ch)):
        j = i
        # print('i=', i, len_dict)
        while j < len(main_ch):
            # print('  j=', j, main_ch[i:j+1], list(t))
            if l2_in_l1(main_ch[i:j + 1], list(t)):

                len_w = ind_list[j] - ind_list[i]
                if (len_w not in len_dict) and (len_w < min_len):
                    len_dict[len_w] = [ind_list[i], ind_list[j]]
                    min_len = len_w
            j += 1

    return s[len_dict[min_len][0]: len_dict[min_len][1] + 1] if len(len_dict) > 0 else ""

print(minWindow_1('aaabbbbcaccdd', 'abcdd'))