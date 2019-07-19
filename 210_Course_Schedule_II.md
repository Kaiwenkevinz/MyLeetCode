### 题目
```
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
```
```
Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
```
```
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
```

### 思路
使用拓扑排序，[步骤](https://github.com/cofo-coding-camp/Kaiwenzhang/blob/master/207-Course-Schedule.md)

### 代码
```py
import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        G = {}
        for i in range(numCourses):
            G[i] = []
        for c, p in prerequisites:
            G[c].append(p)
        
        queue = collections.deque()
        result = []
        
        # find vertices with no indegree
        for c, p in G.items():
            if len(p) == 0:
                queue.append(c)
        
        while queue:
            current_c = queue.popleft()
            result.append(current_c)
            
            for c, p in G.items():
                # remove its edges
                if current_c in p:
                    p.remove(current_c)
                    if len(p) == 0:
                        queue.append(c)
        
        if (len(result) != numCourses):
            return []
        
        return result
    ```
