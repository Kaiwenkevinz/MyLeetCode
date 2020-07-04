### 题目
```
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
 

限制：

2 <= n <= 100000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
```

### 思路
遍历数组，利用hash table找出重复的数字。

遍历数组花费O(n)，hash table的insert和find每次花费O(1), 时间复杂度O(n)

空间复杂度O(n)，因为需要维护一个hash table

### 代码
```py
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            if n in dic:
                return n
            dic[n] = 1
```

### 思路
先排序，然后原地遍历数组，时间复杂度O(nlogn),空间复杂度O(1)

### 代码
```py
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
```
