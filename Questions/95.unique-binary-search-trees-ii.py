#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        if n == 0:
            return []
        
        return self.generateTreesHelper(1, n)
    
    def generateTreesHelper(self, start: int, end: int) -> List[TreeNode]:

        if start > end:
            return [None]
        
        res = []
        for cur_root in range(start, end + 1):
            left = self.generateTreesHelper(start, cur_root - 1)
            right = self.generateTreesHelper(cur_root + 1, end)
            for l in left:
                for r in right:
                    root = TreeNode(cur_root)
                    root.left = l
                    root.right = r
                    res.append(root)

        return res

# @lc code=end

