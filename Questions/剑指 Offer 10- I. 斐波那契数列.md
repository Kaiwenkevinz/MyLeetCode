### 题目
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof

### 思路
迭代，哈希表, 时间空间都是O(n)

```py
class Solution:
    def fib(self, n: int) -> int:

        cache = {}
        cache[0] = 0
        cache[1] = 1

        for i in range(2, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[n] % 1000000007
```

递归，把哈希表改成了integer variable，更省空间
```py
class Solution:
    def fib(self, n: int) -> int:

        if (n == 0 or n == 1):
            return n

        a = 0
        b = 1

        for _ in range(2, n + 1):
            c = a + b
            a = b
            b = c
        
        return b % 1000000007
```

### 思路
递归 + 哈希表，比暴力递归节省一些时间。

```py
class Solution:
    def fib(self, n: int) -> int:

        cache = {}

        return self.helper(n, cache)
    
    def helper(self, n: int, cache: {}):

        if n == 0 or n == 1:
            return n
        
        if n in cache:
            return cache[n]
        
        cache[n] = self.helper(n - 1, cache) + self.helper(n - 2, cache)

        return cache[n] % 1000000007
```
