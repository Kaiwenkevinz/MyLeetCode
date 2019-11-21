### 题目
```
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
```
```
Example 1:

Input: [2,2,1]
Output: 1
```

```
Example 2:

Input: [4,1,2,1,2]
Output: 4
```

### 关键词
- 哈希表
- bit manipulation 位操作


### 解法1-哈希表
```py
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # 时间复杂度 O(n)
        # 空间复杂度 O(size(freq))
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        for k, v in freq.items():
            if v == 1:
                return k
```


### 解法2-位操作
解法过于sao操作，就不放这了

放个网址
https://leetcode.com/problems/single-number/solution/
