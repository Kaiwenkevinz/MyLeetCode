#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        res = []
        reverse = False
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

            if reverse:
                temp.reverse()
                res.append(temp)
                reverse = False
            else:
                res.append(temp)
                reverse = True
            
            cur_level = nex_level
            
        return res
# @lc code=end

