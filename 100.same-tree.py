### 题目
```
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
```

### 关键词
- DFS

### 解法1
```py
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
 ```
