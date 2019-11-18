#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:

        # stack = []
        # for c in s:
        #     if c in ['[', '{', '(']:
        #         stack.append(c)
        #     else:
        #         if c == ']':
        #             if len(stack) == 0 or stack.pop() != '[':
        #                 return False
        #         elif c == '}':
        #             if len(stack) == 0 or stack.pop() != '{':
        #                 return False
        #         elif c == ')':
        #             if len(stack) == 0 or stack.pop() != '(':
        #                 return False

        # if len(stack) == 0:
        #     return True
        # else:
        #     return False

        # dictionary mapping
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for ch in s:
            if ch in mapping:
                if len(stack) == 0 or stack.pop() != mapping[ch]:
                    return False
            else:
                stack.append(ch)
        
        if len(stack) != 0:
            return False

        return True
        
# @lc code=end

