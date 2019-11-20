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

        if not root:
            return []

        res = []
        self.dfs(root, "", res)

        return res

    def dfs(self, root: TreeNode, current: str, res: List[str]) -> None:

        if root.left == None and root.right == None:
            res.append(current + str(root.val))
            return
        
        if root.left != None:
            self.dfs(root.left, current + str(root.val) + "->", res)

        if root.right != None:
            self.dfs(root.right , current + str(root.val) + "->", res)
        
# @lc code=end

