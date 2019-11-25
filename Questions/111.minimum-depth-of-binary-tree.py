#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        return self.helper(root)

    def helper(self, root: TreeNode) -> int:

        if root == None:
            return 0
        
        if root.left == None or root.right == None:
            leftHeight = self.helper(root.left)
            rightHeight = self.helper(root.right)
            return leftHeight + rightHeight + 1
        
        leftHeight = self.helper(root.left)
        rightHeight = self.helper(root.right)

        return min(leftHeight, rightHeight) + 1
        
# @lc code=end

