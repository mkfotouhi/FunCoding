"""
Passing Yearbooks
There are n students, numbered from 1 to n, each with their own yearbook. They would like to pass their yearbooks around and get them signed by other students.
You're given a list of n integers arr[1..n], which is guaranteed to be a permutation of 1..n (in other words, it includes the integers from 1 to n exactly once each, in some order). The meaning of this list is described below.
Initially, each student is holding their own yearbook. The students will then repeat the following two steps each minute: Each student i will first sign the yearbook that they're currently holding (which may either belong to themselves or to another student), and then they'll pass it to student arr[i-1]. It's possible that arr[i-1] = i for any given i, in which case student i will pass their yearbook back to themselves. Once a student has received their own yearbook back, they will hold on to it and no longer participate in the passing process.
It's guaranteed that, for any possible valid input, each student will eventually receive their own yearbook back and will never end up holding more than one yearbook at a time.
You must compute a list of n integers output, whose element at i-1 is equal to the number of signatures that will be present in student i's yearbook once they receive it back.
Signature
int[] findSignatureCounts(int[] arr)
Input
n is in the range [1, 100,000].
Each value arr[i] is in the range [1, n], and all values in arr[i] are distinct.
Output
Return a list of n integers output, as described above.
Example 1
n = 2
arr = [2, 1]
output = [2, 2]
Pass 1:
Student 1 signs their own yearbook. Then they pass the book to the student at arr[0], which is Student 2.
Student 2 signs their own yearbook. Then they pass the book to the student at arr[1], which is Student 1.
Pass 2:
Student 1 signs Student 2's yearbook. Then they pass it to the student at arr[0], which is Student 2.
Student 2 signs Student 1's yearbook. Then they pass it to the student at arr[1], which is Student 1.
Pass 3:
Both students now hold their own yearbook, so the process is complete.
Each student received 2 signatures.
Example 2
n = 2
arr = [1, 2]
output = [1, 1]
Pass 1:
Student 1 signs their own yearbook. Then they pass the book to the student at arr[0], which is themself, Student 1.
Student 2 signs their own yearbook. Then they pass the book to the student at arr[1], which is themself, Student 2.
Pass 2:
Both students now hold their own yearbook, so the process is complete.
Each student received 1 signature.
"""


# Add any extra import statements you may need here


# Add any helper functions you may need here


def findSignatureCounts(arr):
    # Write your code here
    n = len(arr)
    count = 0
    initial = [i for i in range(1, n + 1)]
    holding = initial
    repeat = 1
    dict_switch = dict()
    for i in range(n):
        dict_switch[arr[i]] = i

    print(dict_switch)
    while repeat < 2:
        # print(f'holding:{holding}, initial: {initial}')
        holding = [holding[dict_switch[i + 1]] for i in range(n)]
        # print(' -> holding:', holding)

        if holding == initial:
            repeat += 1
        count += 1
        # print(f'repeat:{repeat}, counter:{count}')
        # print()
    return [count] * n


print(findSignatureCounts([3, 1, 2]))

"""
Contiguous Subarrays
You are given an array arr of N integers. For each index i, you are required to determine the number of contiguous subarrays that fulfill the following conditions:
The value at index i must be the maximum element in the contiguous subarrays, and
These contiguous subarrays must either start from or end on index i.
Signature
int[] countSubarrays(int[] arr)
Input
Array arr is a non-empty list of unique integers that range between 1 to 1,000,000,000
Size N is between 1 and 1,000,000
Output
An array where each index i contains an integer denoting the maximum number of contiguous subarrays of arr[i]
Example:
arr = [3, 4, 1, 6, 2]
output = [1, 3, 1, 5, 1]
Explanation:
For index 0 - [3] is the only contiguous subarray that starts (or ends) with 3, and the maximum value in this subarray is 3.
For index 1 - [4], [3, 4], [4, 1]
For index 2 - [1]
For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
For index 4 - [2]
So, the answer for the above input is [1, 3, 1, 5, 1]
"""


def count_subarrays(arr):
    # Write your code here
    out = []
    for i in range(len(arr)):
        # print()
        check = True
        count = 1
        ind_r = i
        ind_l = i
        val = arr[i]
        r_check = True
        l_check = True
        while check:
            # print(f'  i:{i}, val:{val}, count:{count}')
            # print(f'  ind_l:{ind_l}, ind_r:{ind_r}, r_check={r_check}, l_check={l_check}')
            # print('  ------')

            if (ind_r + 1 < len(arr)) and (arr[ind_r + 1] < val):
                ind_r += 1
                count += 1
            else:
                r_check = False
            if (ind_l - 1 >= 0) and (arr[ind_l - 1] < val):
                ind_l -= 1
                count += 1
            else:
                l_check = False
            check = r_check or l_check
        out.append(count)
    return out


print(count_subarrays([3, 4, 1, 6, 2]))

"""
Rotational Cipher
One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.
Given a string and a rotation factor, return an encrypted string.
Signature
string rotationalCipher(string input, int rotationFactor)
Input
1 <= |input| <= 1,000,000
0 <= rotationFactor <= 1,000,000
Output
Return the result of rotating input a number of times equal to rotationFactor.
Example 1
input = Zebra-493?
rotationFactor = 3
output = Cheud-726?
Example 2
input = abcdefghijklmNOPQRSTUVWXYZ0123456789
rotationFactor = 39
output = nopqrstuvwxyzABCDEFGHIJKLM9012345678
"""


def rotationalCipher(input, rotation_factor):
    # Write your code here
    out = ""
    for ch in input:
        print('----------------')
        print('char:', ch)
        if ch.isdigit():
            r = rotation_factor % 10
            out = out + chr(ord('0') + (ord(ch) - ord('0') + r) % 10)
            print(f'   ch is digit, r={r}, out={out}')
        elif ch.isalpha():
            r = rotation_factor % 26
            is_upper = True
            if ch.islower():
                is_upper = False
            cur = ch.lower()
            cur = chr(ord('a') + (ord(cur) - ord('a') + r) % 26)
            print(f'   ch is alpha, r={r}, isupper={is_upper}, cur={cur}')
            if is_upper:
                cur = cur.upper()
            out = out + cur
            print(f'   out={out}')
        else:
            out = out + ch

    return out

print(rotationalCipher("All-convoYs-9-be:Alert1.", 4)) # "Epp-gsrzsCw-3-fi:Epivx5."


"""
Matching Pairs
Given two strings s and t of length N, find the maximum number of possible matching pairs in strings s and t after swapping exactly two characters within s.
A swap is switching s[i] and s[j], where s[i] and s[j] denotes the character that is present at the ith and jth index of s, respectively. The matching pairs of the two strings are defined as the number of indices for which s[i] and t[i] are equal.
Note: This means you must swap two characters at different indices.
Signature
int matchingPairs(String s, String t)
Input
s and t are strings of length N
N is between 2 and 1,000,000
Output
Return an integer denoting the maximum number of matching pairs
Example 1
s = "abcd"
t = "adcb"
output = 4
Explanation:
Using 0-based indexing, and with i = 1 and j = 3, s[1] and s[3] can be swapped, making it  "adcb".
Therefore, the number of matching pairs of s and t will be 4.
Example 2
s = "mno"
t = "mno"
output = 1
Explanation:
Two indices have to be swapped, regardless of which two it is, only one letter will remain the same. If i = 0 and j=1, s[0] and s[1] are swapped, making s = "nmo", which shares only "o" with t.
"""


def matching_pairs(s, t):
    # Write your code here
    max_count = 0

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            # print(i, j)
            temp = list(s)
            temp[i], temp[j] = temp[j], temp[i]
            count = 0
            for k in range(len(t)):
                if temp[k] == t[k]:
                    count += 1
            if count > max_count:
                max_count = count
    return max_count

print(matching_pairs("abcd", "adcb"))
print(matching_pairs("abcd", "abcd"))



def matching_pairs_n(s, t):
    # Write your code here
    pair_off = set()
    s_off = set()
    t_off = set()
    count = 0
    search_flag = True
    for i in range(len(s)):
        if s[i] == t[i]:
            count += 1
        else:
            if not search_flag:
                continue
            pair_off.add((s[i], t[i]))
            s_off.add(s[i])
            t_off.add(t[i])
            if (t[i], s[i]) in pair_off:
                count += 2
                search_flag = False
            elif (s[i] in t_off) or (t[i] in s_off):
                count += 1



print(matching_pairs_n("abcd", "adcb"))
print(matching_pairs_n("abcd", "abcd"))