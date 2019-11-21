#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = len(nums) - 2
        while i >= 0:
            n = nums[i]
            rest_nums = nums[i + 1: ]
            min_rest_nums_index = self.getMinIndex(rest_nums, len(nums), n)

            if min_rest_nums_index:
                if n < nums[min_rest_nums_index]:
                    nums[i] = nums[min_rest_nums_index]
                    nums[min_rest_nums_index] = n
                    nums[i+1:] = sorted(nums[i+1:])
                    return
            i -= 1
        
        nums.sort()
        return

    # find the number that is minimum in nums and larger than n
    def getMinIndex(self, nums: List[int], length: int, n: int) -> int:
        sorted_nums = sorted(nums)
        for e in sorted_nums:
            if e > n:
                return length - len(nums) + nums.index(e)
        
        return None

        
# @lc code=end

