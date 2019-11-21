#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:

    # Divide and Conquer

    def myPow(self, x: float, n: int) -> float:

        res = self.myPowHelper(x, abs(n))
        
        if n < 0:
            res = 1 / res
            return res
        
        return res

    def myPowHelper(self, x: float, n: int) -> float:

        # base case
        if n == 0:
            return 1
        
        # n is even 
        if n % 2 == 0:
            res = self.myPowHelper(x, n / 2)
            res = res * res
            return res

        # n is odd
        else:
            return x * self.myPowHelper(x, n - 1)

# @lc code=end

