# 哈希表
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # 解法 1
        # 时间复杂度 O(n)
        # 空间复杂度 O(size(freq))
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        for k, v in freq.items():
            if v == 1:
                return k