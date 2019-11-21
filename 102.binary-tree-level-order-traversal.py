#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
# Use a list to keep track of all nodes in one level
# Time: O(n)
# Space: O(n)
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        res = []

        if not root:
            return res

        cur_level = [root]

        while len(cur_level) > 0:

            nex_level = []
            temp = []

            for node in cur_level:
                temp.append(node.val)
                if node.left != None:
                    nex_level.append(node.left)
                if node.right != None:
                    nex_level.append(node.right)

            res.append(temp)
            cur_level = nex_level

        return res
            
# @lc code=end

