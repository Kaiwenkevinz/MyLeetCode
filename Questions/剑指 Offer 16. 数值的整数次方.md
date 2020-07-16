### 题目
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

示例 1:

输入: 2.00000, 10
输出: 1024.00000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof

### 思路
快速幂，把幂当成二进制，时间 O(logN)，空间O(1)

如果用c++或Java，使用int类型会造成数值溢出问题，需要改用long

### 代码
```py
class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n
        
        res = 1
        while n != 0:
            # check if the last digit of binary n is 1
            if n & 1 == 1:
                res *= x
            else:
                res *= 1   # ex. 3^4 * 0^3 * 3^2 * 0^1, 此步骤代表 0^x, 可以省略

            x *= x

            # shift bin n right by 1 digit
            n >>= 1 

        return res
```

### 拓展
long类型的数值边界:
  - unsigned long: 最大值 2 ** 64 - 1， 最小值 0
  - signed long： 最大值 2 ** 63 - 1，最小值 -2 ** 63
