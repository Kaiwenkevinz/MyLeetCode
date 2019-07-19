### 题目
```
Given an array of strings, group anagrams together.
```
```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```
```
Note:

All inputs will be in lowercase.
The order of your output does not matter.
```

### 解法一（超时）
暴力解法，每次从list中拿一个单词，和list中剩下的单词一个一个比较。

存在单词被重复比较的问题，再加上list.remove()是O(n), 所以时间复杂度到了O(n^3)，妥妥的超时。

另外 dic.copy() 增加了空间复杂度。


```py
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
```


### 解法一改进版 (依旧超时）
记录下每个单词是否被比较过，移除了dic.remove(), dic.copy()

时间复杂度减小到O(nk)，但还是超时。。

```py
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}
        res = []
        used = [False] * len(strs)
        i = 0
        
        while i < len(strs):
            anagrams = []
            if (used[i] == False):
                anagrams.append(strs[i])   
                used[i] = True

                j = i + 1
                while j < len(strs):
                    if used[j] == False and self.equal(strs[i], strs[j]):
                        anagrams.append(strs[j])
                        used[j] = True
                    j += 1          
                res.append(anagrams)
            i += 1
        
        return res
    
    def equal(self, str1, str2):
        dic = {}
        for c1 in str1:
            if c1 in dic:
                dic[c1] += 1
            else:
                dic[c1] = 1
        
        for c2 in str2:
            if c2 in dic:
                dic[c2] -= 1
            else:
                return False
        
        for v in dic.values():
            if v != 0:
                return False
    
        return True
```

### 解法二
