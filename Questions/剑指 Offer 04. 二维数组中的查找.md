### 题目
```
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

 

限制：

0 <= n <= 1000

0 <= m <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
```

### 思路
遍历列表，检查是否存在target， O(nm)

```py
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # O(nm)
        for e in matrix:
            if target in e:
                return True

        return False
```

### 思路
遍历每一行，用二分查找，O(nlogm)

```py
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:

        # check if target may be in the inner list
        # if probably in the inner list, use binary search
        # O(nlogm)

        for e in matrix:
            # binary search
            l = 0
            r = len(e) - 1
            while l <= r:
                m = (l + r) // 2
                if target > e[m]:
                    l = m + 1
                elif target < e[m]:
                    r = m - 1
                else:
                    return True
        return False
```

### 思路
利用此二维数组是递增的特性，从右上角往左下角开始查找。
O(n+m)

```py
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # start from top right
        # if target < cur, go left
        # if target > cur, go down
        # stop when find target, or when current position < 0 after went left, or when current position > length of matrix - 1 after went down

        # special case
        # []
        if len(matrix) == 0:
            return False

        i_row = 0
        i_col = len(matrix[0]) - 1

        while i_row < len(matrix) and i_col >= 0:
            if target == matrix[i_row][i_col]:
                return True
            elif target > matrix[i_row][i_col]:
                i_row += 1
            else:
                i_col -= 1
        
        return False
```
