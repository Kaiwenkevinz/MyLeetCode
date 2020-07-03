### 题目 
https://www.nowcoder.com/practice/5afcf93c419a4aa793e9b325d01957e2?tpId=137&&tqId=33898&rp=1&ru=/ta/exam-bytedance&qru=/ta/exam-bytedance/question-ranking

### 思路
本题类似于在一组数中找出数字的最大连续出现次数，不同的是数组由一维数组（int）变成二维数组（int，int）。

因为需要记录frequency，想到用哈希表记录出现频率。因为需要记录是否连续出现，想到再用一个哈希表记录出现的位置。

还有一个难点是对于臭长的input的处理，用 sys.stdin.readline().strip(), 注意这里返回的是string，必要时用split() 转化为list再操作，

注意split()后还是 a list of strings, 用 list(map(int, xxx)) 转化为 a list of int。别忘了 import sys。

map(int, xxx) returns an iterator, 用list(iterator) 转化为 list。

### 代码
``` py
import sys

def main(x):
    freq_map = {} # ((int, int), int) number of times appeared continuously
    pos_map = {}  # ((int, int), int) position of line that first appeared continuously
    res = 1
    
    # O(Mn)
    for line_i in range(len(x)):
        line = x[line_i]
        for feature in line:
            # check if feature appears in last line
            # if in last line, update freq_map
            # else, update pos_map, update res
            if feature in pos_map:
                # appears in last line
                if line_i - pos_map[feature] == freq_map[feature]:
                    freq_map[feature] += 1
                    res = max(res, freq_map[feature])
                # did not appear in last line
                else:
                    pos_map[feature] = line_i
                    res = max(res, freq_map[feature])
                    freq_map[feature] = 1
            else:
                pos_map[feature] = line_i
                freq_map[feature] = 1
    print(res)

N = int(sys.stdin.readline().strip())
for i in range(N):
    M = int(sys.stdin.readline().strip())
    case = []
    for k in range(M):
        line = list(map(int, sys.stdin.readline().strip().split()))
        num_feature = line[0]
        one_line = []
        for y in range(num_feature):
            one_line.append((line[2 * y + 1], line[2 * y + 2]))
        case.append(one_line)
    main(case)
```

### 时间复杂度
处理input的两个for loop的复杂度为 O(NM), main()中对哈希表的读写为 O(n)
    
