#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        return self.helper(preorder, inorder, 0, 0, len(inorder) - 1)
    
    def helper(self, preorder: List[int], inorder: List[int], preIndex: int, inStart: int, inEnd: int) -> TreeNode:

        if preIndex >= len(preorder) or inStart > inEnd:
            return
        
        root = preorder[preIndex]
        rootIndex = inorder.index(root)

        leftSubStartIndex = inStart
        leftSubEndIndex = rootIndex - 1
        leftSubRootIndex = preIndex + 1

        rightSubStartIndex = rootIndex + 1
        rightSubEndIndex = inEnd
        rightSubRootIndex = preIndex + leftSubEndIndex - leftSubStartIndex + 1 + 1

        node = TreeNode(root)
        node.left = self.helper(preorder, inorder, leftSubRootIndex, leftSubStartIndex, leftSubEndIndex)
        node.right = self.helper(preorder, inorder, rightSubRootIndex, rightSubStartIndex, rightSubEndIndex)

        return node 
        
# @lc code=end

