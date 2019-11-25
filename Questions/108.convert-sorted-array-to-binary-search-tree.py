#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(n)
# Spaec: O(n)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        if nums == [] or not nums:
            return None

        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums: List[int], start: int, end: int):

        if start > end:
            return
        
        rootIndex = (end - start) // 2 + start
        root = nums[rootIndex]
        node = TreeNode(root)

        node.left = self.helper(nums, start, rootIndex - 1)
        node.right = self.helper(nums, rootIndex + 1, end)

        return node
# @lc code=end

