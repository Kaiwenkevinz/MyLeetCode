### 题目
```
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

 

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
```

### 思路 （递归)
前序遍历特点：第0个node一定是root

中序遍历特点：只要知道root的值，就知道了root的所有左子树的个数和值和所有右子树的个数和值

根据前序遍历，得root的值，再根据中序遍历，得root的所有左右字数的值（乱序），再根据前序遍历和所有右子树的node个数，得root的左右子树的root。  
此时已知root，left subtree root和right subtree root，
一个小tree就有了。  
就此打住，如果再往下细想脑子就炸了（反正我是），直接开始递归，最后返回大树的top root 
 
时间复杂度： O(n). create_hash_table() 花费 O(n)，递归花费 O(n), 递归中的操作花费 O(1)  
空间复杂度： O(n). hash table 和 递归调用栈各花费 O(n)

### 代码
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        # Special case: input is either None or an empty tree
        if (preorder == None or inorder == None or len(preorder) == 0 or len(inorder) == 0):
            return None

        # hash table {inorder value, inorder index}
        # used for quickly finding index
        self.inorder_value_index_table = self.create_hash_table(inorder)

        # start recursion
        root = self.helper(preorder, inorder, 0, 0, len(inorder) - 1)

        return root
            
    # preorder: the provided preorder list
    # inorder: the provided inorder list
    # preorder_root_i: the root index in preorder list
    # left_i: the left bound of the sub left tree
    # right_i: the right bound of the sub right tree
    # Return: Root node of the tree
    def helper(self, preorder: List[int], inorder: List[int], preorder_root_i: int, left_i: int, right_i: int) -> TreeNode:

        # base case
        if left_i > right_i or preorder_root_i >= len(preorder):
            return None

        root_value = preorder[preorder_root_i]
        
        inorder_root_i = self.inorder_value_index_table[root_value]
        root = TreeNode(root_value)

        root.left = self.helper(preorder, inorder, preorder_root_i + 1, left_i, inorder_root_i - 1)
        root.right = self.helper(preorder, inorder, preorder_root_i + (inorder_root_i - left_i + 1), inorder_root_i + 1, right_i)

        return root

    def create_hash_table(self, inorder: List[int]) -> {}:
        dic = {}
        i = 0
        for e in inorder:
            dic[e] = i
            i += 1
        
        return dic

```

### 思路（迭代）

### 代码
