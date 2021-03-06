# *******************************************************
# ************  problem 10   (13 on LeetCode)  *************
# *******************************************************
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. CMXCIX



Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""
def romanToInt_mkf(s: str) -> int:
    """
    Runtime: 61 ms, faster than 31.83% of Python3 online submissions for Roman to Integer.
    Memory Usage: 14.4 MB, less than 28.23% of Python3 online submissions for Roman to Integer.
    """
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    val = 0
    for i in range(len(s)):
        if i + 1 < len(s):
            if roman_dict[s[i]] >= roman_dict[s[i + 1]]:
                val += roman_dict[s[i]]
            else:
                val += - roman_dict[s[i]]
        else:
            val += roman_dict[s[i]]
    return val


print(romanToInt_mkf('VII'))
print(romanToInt_mkf('XXII'))
print(romanToInt_mkf('IX'))
print(romanToInt_mkf('CM'))
print(romanToInt_mkf('XC'))

s="XXII"

def romanToInt_salman(s: str) -> int:
    list_s = list(s)
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D":500, "M": 1000}
    temp = roman[list_s[0]]
    value = temp
    for letter in list_s[1:]:
        if temp < roman[letter] :
            value += roman[letter] - 2 * temp
        else:
            value += roman[letter]
            temp = roman[letter]
    return value

romanToInt_salman(s)


def romanToInt_fati(s: str) -> int:

    dic_roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    index_roman = {"I": 0, "V": 1, "X": 2, "L": 3, "C": 4, "D": 5, "M": 6}

    list_s = list(s)
    sum_rom = 0
    while list_s:
        if len(list_s) > 1:
            if index_roman[list_s[0]] < index_roman[list_s[1]]:
                sum_rom += (dic_roman[list_s[1]] - dic_roman[list_s[0]])
                list_s.pop(1)
                list_s.pop(0)
            else:
                sum_rom += dic_roman[list_s[0]]
                list_s.pop(0)
        else:
            sum_rom += dic_roman[list_s[0]]
            list_s.pop(0)
    return sum_rom

print(romanToInt_fati("MCMXCIV"))

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




def longestCommonPrefix_mkf(strs):
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


#out = longestCommonPrefix_mkf(["flower", "flow", "flight"])
#print(out)
#out = longestCommonPrefix_mkf(['car', ''])
#print(out)
#out = longestCommonPrefix_mkf(["flower"])
#print(out)


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

#print(fati_sal(["flow","flow"]))


def longestCommonPrefix_Salman( strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    size = len(strs)
    if size == 0:
        return ""
    if size == 1:
        return strs[0]
    strs.sort()
    end = min(len(strs[0]), len(strs[size - 1]))

    i = 0
    while (i < end and
           strs[0][i] == strs[size - 1][i]):
        i += 1

    output = strs[0][:i]
    return output

#longestCommonPrefix_Salman(["flower","flow","flight"])


