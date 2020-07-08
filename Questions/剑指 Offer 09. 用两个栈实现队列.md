### 题目
```
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：

1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
```

### 思路
一个栈作为主栈，一个栈作为辅助栈，每次append到主栈，delete时把主栈的元素都移到副栈，这样主栈的head就成了副栈的tail，remove tail，再把剩下的元素移回主栈。

空间复杂度 O(n)。 需要维护两个栈。

时间复杂度 Append - O(1), Delete - O(n)。Delete的运行速度较慢，需要来回在两栈之间移动所有元素。

### 代码
```py
class CQueue:

    def __init__(self):
        self.main_s = [] # stack
        self.temp_s = [] # another stack for temp use

    # O(1)
    def appendTail(self, value: int) -> None:
        self.main_s.append(value)

    # O(n)
    def deleteHead(self) -> int:
        if self.main_s == []:
            return -1

        # move elements in main stack to temp stack
        while self.main_s != []:
            self.temp_s.append(self.main_s.pop())
        
        v = self.temp_s.pop()

        # restore back
        while self.temp_s != []:
            self.main_s.append(self.temp_s.pop())

        return v


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
```

### 思路
和上个思路差不多，唯一区别就在每次delete的时候不需要来回倒stack，只要temp stack不是空的，那直接pop就行，直到temp stack是空的的时候再从 main stack 倒。
###

```py
class CQueue:

    def __init__(self):
        self.main_s = [] # stack
        self.temp_s = [] # another stack for temp use

    # O(1)
    def appendTail(self, value: int) -> None:
        self.main_s.append(value)

    # O(n)
    def deleteHead(self) -> int:
        if self.temp_s == [] and self.main_s == []:
            return -1

        if self.temp_s == []:
            # move elements in main stack to temp stack
            while self.main_s != []:
                self.temp_s.append(self.main_s.pop())

        return self.temp_s.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
```
