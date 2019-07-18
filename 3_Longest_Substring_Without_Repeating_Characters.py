# 滑动窗口
# 时间复杂度 O(n)
# 空间复杂度 O(size([0]*128))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
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
