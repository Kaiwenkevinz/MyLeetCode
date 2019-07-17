import string
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) < 2:
            return len(s)
        
        # dictionary of the alphabet
        # key: letter
        # value: count of appearence
        dic = {}
        for i in range(129):
            dic[chr(i)] = 0
        print(dic)
        # dic = dict.fromkeys(string.ascii_lowercase, 0)
        
        # store the length of longest substring
        result = 1
        
        index_outter = 0
        index_inner = 1
        while index_outter < len(s):
            dic[s[index_outter]] = index_outter
            while index_inner < len(s):  
                print(s[index_inner])
                print(dic[s[index_inner]])
                if dic[s[index_inner]] != 0:
                    #print(str(index_inner) + " " + str(index_outter))
                    result = max(result, index_inner - dic[s[index_inner]])
                    dic[s[index_inner]] = index_inner
                    break
                elif index_inner == len(s) - 1:
                    # print(str(index_inner) + " " + str(index_outter))
                    result = max(result, index_inner - index_outter)
                    return result
                else:
                    dic[s[index_inner]] = index_inner
                    index_inner += 1
            index_outter += 1
            dic = dict.fromkeys(string.ascii_lowercase, 0)

        return result
