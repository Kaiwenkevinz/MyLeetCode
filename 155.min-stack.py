#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:
    
    # def __init__(self):
    #     self.data = []
    #     self.minimum = None

    # def push(self, x: int) -> None:
    #     self.data.append(x)

    #     if self.minimum == None:
    #         self.minimum = x
    #     elif x < self.minimum:
    #          self.minimum = x

    # def pop(self) -> None:
    #     n = self.data[-1]       
    #     del self.data[-1]

    #     if n == self.minimum:
    #         self.updateMin()

    #     return n

    # def updateMin(self) -> None:
    #     if len(self.data) == 0:
    #         self.minimum = None
    #     else:
    #         self.minimum = self.data[0]
    #         for n in self.data:
    #             self.minimum = min(n, self.minimum)

    # def top(self) -> int:

    #     return self.data[-1]
        
    # def getMin(self) -> int:

        # return self.minimum

    # Method 2
    # faster, more memory usage
    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        if len(self.data) == 0:
            self.data.append((x, x))
        else:
            self.data.append((x, min(x, self.data[-1][1])))

    def pop(self) -> None:
        n = self.data[-1][0]
        del self.data[-1]

        return n

    def top(self) -> int:
        return self.data[-1][0]
        
    def getMin(self) -> int:
        return self.data[-1][1]

# @lc code=end

