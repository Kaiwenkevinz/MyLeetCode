#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        return self.helper(inorder, postorder, len(postorder) - 1, 0, len(postorder) - 1)
        
    def helper(self, inorder: List[int], postorder: List[int], postIndex: int, inStart: int, inEnd: int) -> TreeNode:

        if postIndex < 0 or inStart > inEnd:
            return

        root = postorder[postIndex]
        rootIndex = inorder.index(root)

        node = TreeNode(root)

        node.left = self.helper(inorder, postorder, postIndex - (inEnd - (rootIndex + 1) + 1 ) - 1, inStart, rootIndex - 1)
        node.right = self.helper(inorder, postorder, postIndex - 1, rootIndex + 1, inEnd)

        return node

# @lc code=end

