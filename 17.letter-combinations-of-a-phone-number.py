#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:

    dic = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        res = []
        self.letterCombinationsDFS(digits, 0, "", res)

        return res

    def letterCombinationsDFS(self, digits, index, current, res):

        # base case
        # stop recursion when pass the last digit
        if (index == len(digits)):
            res.append(current)
            return
        
        for letter in self.dic[digits[index]]:
            self.letterCombinationsDFS(digits, index + 1, current + letter, res)
        
# @lc code=end

