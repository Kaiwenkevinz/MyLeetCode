#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
            
        while n >= 2 and n % 2 == 0:
            n = n / 2
        
        if n == 1:
            return True
        else:
            return False
        
# @lc code=end

