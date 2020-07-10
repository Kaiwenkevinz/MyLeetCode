### 题目
```
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
```

### 思路
遍历，时间 O(n)，空间 O(1)

```py
class Solution:
    def minArray(self, numbers: List[int]) -> int:

        if numbers == []:
            return 

        for i in range(len(numbers) - 1):
            if numbers[i + 1] < numbers[i]:
                return numbers[i + 1]
        
        return numbers[0]
```

### 思路
二分查找法，时间复杂度降低到 O(logN).

```py
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        i = 0
        j = len(numbers) - 1

        while i < j:
            mid = (i + j) // 2
            if numbers[mid] > numbers[j]:
                i = mid + 1
            elif numbers[mid] < numbers[j]:
                j = mid
            else:
                j -= 1

        return numbers[i]
```
