#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start

# Method: DP
# state: [i]
# init: dp[0] = dp[1] = 1
# func: 
# result: [n]

# Time: O(n^2)
# Space: O(n)
class Solution:
    def numTrees(self, n: int) -> int:

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            for j in range(0, i):
                dp[i] += dp[i - j - 1] * dp[j]
        
        return dp[n]
        
# @lc code=end

