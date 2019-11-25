#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        return self.helper(root) != -1
    
    def helper(self, root: TreeNode) -> int:

        if root == None:
            return 0
        
        left_height = self.helper(root.left)
        right_height = self.helper(root.right)

        if abs(left_height - right_height) > 1 or left_height == -1 or right_height == -1:
            return -1
        
        return max(left_height, right_height) + 1

        
# @lc code=end

