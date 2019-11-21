#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(n)
# Space: O(n)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        res = [0]
        self.dfs(root, 0, res)

        return res[0]
    
    def dfs(self, root: TreeNode, cur_count: int, res: List[int]):
        
        if root == None:
            return
        
        if root.left == None and root.right == None:
            cur_count += 1
            res[0] = max(res[0], cur_count)
            return
        
        if root.left != None:
            self.dfs(root.left, cur_count + 1, res)

        if root.right != None:
            self.dfs(root.right, cur_count + 1, res)
        
# @lc code=end

