# *******************************************************
# ***********  problem 6  (155 on LeetCode)  ************
# *******************************************************
"""
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Constraints:

-2^31 <= val <= 2^31 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""


class MinStack_mkf:
    """
    Runtime: 100 ms, faster than 32.66% of Python3 online submissions for Min Stack.
    Memory Usage: 18.4 MB, less than 26.42% of Python3 online submissions for Min Stack.
    """
    def __init__(self):
        self.vals = dict()
        self.min = None
        self.len = 0

    def push(self, val: int) -> None:
        self.vals[self.len] = val
        self.len += 1
        if self.min is not None:
            self.min = min(self.min, val)
        else:
            self.min = val

    def pop(self) -> None:
        self.len -= 1
        out = self.vals[self.len]
        del self.vals[self.len]
        if out == self.min:
            if len(self.vals) > 0:
                self.min = min(list(self.vals.values()))
            else:
                self.min = None

    def top(self) -> int:
        return self.vals[self.len - 1]

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
obj = MinStack_mkf()
obj.push(-3)
obj.push(1)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
