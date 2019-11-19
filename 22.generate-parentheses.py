#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.generateParenthesis_helper(n, n, "", res)

        return res
    
    def generateParenthesis_helper(self, num_paren_left, num_paren_right, current, result):
        # Goal: Get valid combination of parentheses of length n * 2
        # Choices: Append "(" or ")" to current
        # Constraint: During each run, number of left paraenthesis <= number of right paraenthesis

        # found one combination
        # return to previous state to find other possibilities
        if (num_paren_left == 0 and num_paren_right == 0):
            result.append(current)
            return
        
        # In what condition can we insert "("?
        # when number of left parenthesis left > 0
        if (num_paren_left > 0):
            self.generateParenthesis_helper(num_paren_left - 1, num_paren_right, current + "(", result)

        # In what condition can we insert ")"?
        # when numeber of right parenthesis left > number of left parenthesis left
        if (num_paren_left < num_paren_right):
            self.generateParenthesis_helper(num_paren_left, num_paren_right - 1, current + ")", result)
        
# @lc code=end