class Solution:
    def isHappy(self, n: int) -> bool:
        
        dic = {}
        int_s = str(n)
        
        while True:
            summ = 0
            for n in int_s:
                n_sq = int(n) * int(n)
                summ += n_sq
            if summ == 1:
                return True
            if int_s in dic:
                return False
            dic[int_s] = summ
            int_s = str(summ)
