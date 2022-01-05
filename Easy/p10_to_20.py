# *******************************************************
# ************  problem 2  (14 on LeetCode)  *************
# *******************************************************
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters."""




def longestCommonPrefix_mkf(self, strs):
    '''
    Runtime: 67 ms, faster than 5.11% of Python3 online submissions for Longest Common Prefix.
    Memory Usage: 14.3 MB, less than 82.17% of Python3 online submissions for Longest Common Prefix.
    '''
    if len(strs) == 1:
        return strs[0]
    pr = ''
    for i in range(len(strs[0])):
        ch = strs[0][i]
        for j in range(1, len(strs)):
            if (len(strs[j]) > i):
                if (strs[j][i] == ch):
                    continue
                else:
                    return pr
            else:
                return pr
        pr += ch

    return pr


out = longestCommonPrefix(["flower", "flow", "flight"])
print(out)
out = longestCommonPrefix(['car', ''])
print(out)
out = longestCommonPrefix(["flower"])
print(out)


def fati_sal(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    output = strs[0] if len(strs)==1 else ''
    letters = ''        
    for i, letter in enumerate(strs[0]):
        letters = letters + letter
        for word in strs[1:]:
            if len(strs[0]) == len(letters):
                output = letters
            if letters != word[:i+1]:
                output = letters[:-1]
                break
        else:
            continue
        break

    return output

print(fati_sal(["flow","flow"]))

