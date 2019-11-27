#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start

# Time: O(nlogn)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # modify parameter in-place
        # i = 0
        # intervals.sort()

        # while i < len(intervals) - 1:
        #     left = intervals[i]
        #     right = intervals[i + 1]

        #     if right[0] <= left[1]:
        #         rightBound = max(left[1], right[1])
        #         new = [left[0], rightBound]
        #         intervals[i] = new
        #         del intervals[i + 1]
        #     else:
        #         i += 1
            
        # return intervals

        res = []
        intervals.sort()

        for interval in intervals:
            if len(res) == 0 or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        
        return res
        
# @lc code=end

