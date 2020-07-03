### 题目
https://www.nowcoder.com/practice/0bb1fad52f474bdaa4d7636ca3a98244?tpId=137&&tqId=33886&rp=1&ru=/ta/exam-bytedance&qru=/ta/exam-bytedance/question-ranking

### 思路
用hash记录每种颜色出现的位置，根据位置得出在连续的 m 个珠子中是否出现过此颜色。

难点在于串是环形的，如何处理最后一个珠子和第一个珠子，这里通过找规律得出 (n - pos_list[-1] + 1) <= m

### 代码
```py
import sys

# take care of input
first_line = list(map(int, sys.stdin.readline().strip().split()))
n = first_line[0]
m = first_line[1]
c = first_line[2]
res = 0

dic = {}   #{color: pos of zhu where this color appears}
for i in range(n):
    line = list(map(int, sys.stdin.readline().strip().split()))
    for c in line[1:]:
        if c in dic:
            dic[c].append(i)
        else:
            dic[c] = [i]

for c, pos_list in dic.items():
    # wrap around
    if (n - pos_list[-1] + 1) <= m:
        res += 1
        continue
        
    for i in range(len(pos_list) - 1):
        if (pos_list[i+1] - pos_list[i]) < m:
            res += 1
            break
            
print(res)
```

### 思路（暴力, 超时）
一个珠子一个珠子的看颜色是否出现多次，灰常的暴力，三个嵌套for loop，灰常的超时。

### 代码 
```py
import sys

# take care of input
first_line = list(map(int, sys.stdin.readline().strip().split()))
n = first_line[0]
m = first_line[1]
c = first_line[2]
input_list = []

for line_i in range(n):
    line = list(map(int, sys.stdin.readline().strip().split()))
    num_i = line[0]
    temp = []
    for i in range(1, num_i + 1):
        temp.append(line[i])
    input_list.append(temp)
    
map_freq = {}
map_appear = {}

for pivot in range(n):
    map_freq.clear()
    for i in range(m):
        real_i = (pivot + i) % n
        e = input_list[real_i]
        for c in e:
            if c in map_freq:
                map_appear[c] = 1
            else:
                map_freq[c] = 1
        
print(len(map_appear))
```
