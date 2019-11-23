#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(n)
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        if root == None:
            return []

        res = []
        cur_level = [root]

        while cur_level:
            temp = []
            nex_level = []

            for node in cur_level:
                temp.append(node.val)
                if node.left: 
                    nex_level.append(node.left)
                if node.right:
                    nex_level.append(node.right)

            res.append(temp)

            cur_level = nex_level
                
        res.reverse()

        return res

        
# @lc code=end

