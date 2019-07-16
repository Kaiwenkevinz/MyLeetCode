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
       #print(result_order)
        return len(result_order) == numCourses