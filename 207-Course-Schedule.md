### 题目
https://leetcode.com/problems/course-schedule/

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

```Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
```
```
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
```

Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

### 思路
此题可以抽象为一个Graph。有n门课，每门课代表Graph中的一个vertex，它的前置课和它形成了一个edge。所以这个Graph实际上就是一个unweighted directed graph。

所以这题可以看成：给一个有向图，检查此图是否有环。
如果无环，return true。有环就return false。

检查一个有向图是否有环的算法步骤：
1. 选一个入度为零的顶点
2. 移除此顶点
3. 移除与此顶点相连的边
4. 重复2,3直到没有入度为零的顶点
5. 如果图中还有顶点，则有环，反之无环

### 代码
```py
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # init graph
        G = {}
        for i in range(numCourses):
            G[i] = []
        for course, prereq in prerequisites:
            G[course].append(prereq)

        # init order list 
        # list: store the order of courses being processed
        # length of order == numCourses means no cycle
        result_order = []
        
        # init working queue
        working_queue = collections.deque()
        
        # put courses without prereq into working_queue
        for course, prereqs in G.items():
            if len(prereqs) == 0:
                working_queue.append(course)
        
        while working_queue:
            working_course = working_queue.popleft()
            result_order.append(working_course)
            
            for course, prereqs in G.items():
                # remove vertice and its connecting edges
                if working_course in prereqs:
                    prereqs.remove(working_course)
                    if len(prereqs) == 0:
                        working_queue.append(course)
                        
        return len(result_order) == numCourses
```
