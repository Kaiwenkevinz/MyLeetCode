### 题目
https://leetcode.com/problems/longest-substring-without-repeating-characters/

```
Given a string, find the length of the longest substring without repeating characters.
```

```
Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
```

```
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

### 关键词
- 滑动窗口
- 左右指针

### 思路

用左右指针维护一个没有重复字母的滑动窗口。 

```
# 伪代码
left = 0
right = -1
res <= the length of the longest substring w/o repeating characters
freq <= the frequency of appearance for each character

while left < len && right+1 < len：
	if character at right+1 appeared before
    	clear its frequency of appearance
        left ++
    else # character is unique
 		update the frequency of the character 
        right ++
    
    length_of_current_substring <= right-left + 1
    res = max(res, length_of_current_substring)
  
return res
```

- 为什么右指针初始化为-1，而不是0?
```
一开始，左右指针形成的滑动窗口是空的。如果右指针初始化为0，会让str[0]出现在初始化的滑动窗口中。
```
- 为什么每次循环要检查位置在right + 1的字母，而不是right位置的字母？
```
right位置是滑动窗口的右边界，检查right+1位置的字母, 如果字母没有出现过，则right++，使字母存入滑动窗口中。
如果检查的是right位置的字母，这说明此时right位置的字母还不确定是不是unique的，也说明滑动窗口的右边界在right-1位置
```

动画效果： https://github.com/MisterBooo/LeetCodeAnimation/blob/master/notes/LeetCode%E7%AC%AC3%E5%8F%B7%E9%97%AE%E9%A2%98%EF%BC%9A%E6%97%A0%E9%87%8D%E5%A4%8D%E5%AD%97%E7%AC%A6%E7%9A%84%E6%9C%80%E9%95%BF%E5%AD%90%E4%B8%B2.md

### 代码
```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
    	# 解法1
    	# 时间复杂度 O(n)
    	# 空间复杂度 O(size([0]*128))
    
        freq = [0] * 128
        
        l = 0
        r = -1
        res = 0
        
        while l < len(s) and r + 1 < len(s):
            # the character right next the slide window is in it
            # move left side, clear the freq of that character
            if freq[ord(s[r+1])] == 1:
                freq[ord(s[l])] -= 1
                l += 1
            else: #the charater right next the slide window is not in the window, put in
                freq[ord(s[r+1])] = 1
                r += 1
                
            res = max(res, r-l+1)
            
        res = max(res, r-l+1)
        
        return res

# 解法2
#         if len(s) < 2:
#             return len(s)
        
#         result = 0
#         dic = {}
        
#         index = 0
#         start = 0
#         cur_len = 0
        
#         while index < len(s):
#             letter = s[index]
#             if letter in dic and dic[letter] >= start:
#                 start = dic[letter]
#                 cur_len = index - dic[letter]
#             else:
#                 cur_len += 1
#             dic[letter] = index
#             result = max(result, cur_len)
#             index += 1

#         return result
```
