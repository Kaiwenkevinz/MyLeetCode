#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        # Method 1 with loop
        # while n >= 3 and n % 3 == 0:
        #     n = n / 3
        
        # return n == 1

        # Method 2 without loop
        return (n > 0 and 3 ** 19 % n == 0)
        
# @lc code=end

