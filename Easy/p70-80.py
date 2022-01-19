# *******************************************************
# ************  problem 12  (70 on LeetCode)  ***********
# *******************************************************
"""
70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
"""
def climbStairs_mkf(n: int) -> int:
    """
    Runtime: 28 ms, faster than 85.44% of Python3 online submissions for Climbing Stairs.
    Memory Usage: 14.3 MB, less than 11.66% of Python3 online submissions for Climbing Stairs.
    """
    memory_dict = dict()
    def tree_depth(n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in memory_dict:
            return memory_dict[n]
        memory_dict[n] = 0
        memory_dict[n] = memory_dict[n] + tree_depth(n - 1)
        memory_dict[n] = memory_dict[n] + tree_depth(n - 2)
        return memory_dict[n]
    return tree_depth(n)


print(climbStairs_mkf(2))
print(climbStairs_mkf(5))
print(climbStairs_mkf(38))

