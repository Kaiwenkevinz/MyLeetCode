### 题目
```
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

 

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof
```
### 思路
Python的string类是immutable的，所以没有使用类似C++的反向遍历+后移。直接创建新string，遍历老string，然后return 新string即可。

时间空间都是o(n)

```py
class Solution:
    def replaceSpace(self, s: str) -> str:
        # Time: O(n)
        # Space: O(n)
        res = ""
        for c in s:
            if c == ' ':
                res += "%20"
            else:
                res += c

        return res
```
