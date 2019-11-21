#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        res_p = []
        res_q = []

        self.dfs(p, "", res_p)
        self.dfs(q, "", res_q)

        return res_p == res_q
    
    def dfs(self, root: TreeNode, current: str, res: List[str]) -> None:

        if root == None:
            current += "E"
            res.append(current)
            return

        self.dfs(root.left, current + str(root.val), res)
        self.dfs(root.right, current + str(root.val), res)

# @lc code=end

