### 题目
```
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
```

### 思路
递归， O(n)

要注意当链表很长时，调用栈可能会溢出，

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:

        if not head:
            return []
            
        res = []
        self.helper(head, res)

        return res
    
    def helper(self, node: ListNode, res: List[int]) -> None:
        if node.next:
            self.helper(node.next, res)
        
        res.append(node.val)
```

### 思路
栈

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:

        order = []
        while head:
            order.append(head.val)
            head = head.next

        res_order = []
        while len(order) > 0:
            res_order.append(order.pop())
            

        return res_order
```
