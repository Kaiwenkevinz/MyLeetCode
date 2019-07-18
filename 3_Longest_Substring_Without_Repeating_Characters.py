class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) < 2:
            return len(s)
        
        result = 0
        dic = {}
        
        index = 0
        start = 0
        cur_len = 0
        
        while index < len(s):
            letter = s[index]
            if letter in dic and dic[letter] >= start:
                start = dic[letter]
                cur_len = index - dic[letter]
            else:
                cur_len += 1
            dic[letter] = index
            result = max(result, cur_len)
            index += 1

        return result
