#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res_list = []

        if root == None:
            return []

        self.binaryTreePathsHelper(root, "", res_list)

        return res_list

    def binaryTreePathsHelper(self, root: TreeNode, current: str, res: List[str]):

        # base case
        if root.left == None and root.right == None :
            current += str(root.val)
            res.append(current)
            return
        
        if root.left != None:
            self.binaryTreePathsHelper(root.left, current + str(root.val) + "->", res)
        if root.right != None:
            self.binaryTreePathsHelper(root.right, current + str(root.val) + "->", res)
            
        
# @lc code=end

