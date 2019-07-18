class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}
        res = []
        
        while len(strs) > 0:
            anagrams = []
            word = strs[0]
            for c in word:
                try:
                    dic[c] += 1
                except:
                    dic[c] = 1
            anagrams.append(word)    
            strs.remove(word)

            i = 0
            while i < len(strs):
                w = strs[i]
                is_anagram = True
                dic_copy = dic.copy()
                for c in w:
                    if c not in dic_copy or dic_copy[c] <= 0 or len(word) != len(w):
                        is_anagram = False
                        break
                    dic_copy[c] -= 1
                if word == "" and w == "":
                    anagrams.append(w)
                    strs.remove(w)
                elif word != "" and w != "" and is_anagram == True:
                    anagrams.append(w)
                    strs.remove(w)
                else:
                    i += 1
            dic = {}
            res.append(anagrams)
        
        return res