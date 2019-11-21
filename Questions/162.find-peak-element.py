#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        if not nums:
            return None

        i = 0
        while i < len(nums):
            if i == 0 and nums[i] > nums[i + 1]:
                return 0
            elif i == len(nums) - 1 and nums[len(nums) - 2] < nums[len(nums) - 1]:
                return i
            else:
                prev = nums[i - 1]
                nex = nums[i + 1]
                n = nums[i]
                if prev < n and n > nex:
                    return i
            i += 1
        
# @lc code=end

