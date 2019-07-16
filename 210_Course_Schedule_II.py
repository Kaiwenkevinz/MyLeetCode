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