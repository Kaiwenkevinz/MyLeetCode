#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# # Recursion, pass lower and upper limit and compare them with root value
# # Time: O(n)
# # Space: O(n)
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:

#         return self.helper(root, float('-inf'), float('inf'))

#     def helper(self, root: TreeNode, lower: int, upper: int) -> bool:

#         if root == None:
#             return True
        
#         if root.val <= lower or root.val >= upper:
#             return False
        
#         return self.helper(root.left, lower, root.val) and self.helper(root.right, root.val, upper)
    

# Iteration DFS
# Use Stack
# Time: O(n)
# Space: O(n)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        stack = []
        lower_bound = float('-inf')

        while stack or root:

            # get all left node
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            
            if root.val <= lower_bound:
                return False
            
            lower_bound = root.val

            # move to right node
            root = root.right
        
        return True

# # Get BST path and compare to sorted version
# # Time: O(nlogn)
# # Space: O(n)
# # could be better
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:

#         if not root:
#             return True

#         res = []
#         self.helper(root, res)

#         res_copy = res[:]
#         res_copy = list(set(res_copy))
#         res_copy.sort()

#         # print(res)
#         # print(res_copy)

#         return res == res_copy and len(res) == len(res_copy)
    
#     def helper(self, root: TreeNode, res: List[int]) -> bool:

#         if root == None:
#             return

#         if root.left != None:
#             self.helper(root.left, res)

#         res.append(root.val)

#         if root.right != None:
#             self.helper(root.right, res)


        
# @lc code=end

