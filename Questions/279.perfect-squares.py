#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
from math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:

        # 四平方之和定理
        while (n % 4 == 0):
            n = n/4
        
        if (n % 8 == 7):
            return 4

        i = 0
        while i * i <= n:
            b = int(sqrt(n - i * i))
            if b*b + i*i == n:
                if b != 0 and i != 0:
                    return 2
                if b != 0 or i != 0:
                    return 1
            i += 1

        
        return 3
        
# @lc code=end

