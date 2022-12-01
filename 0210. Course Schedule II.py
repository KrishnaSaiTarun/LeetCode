from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjs = defaultdict(set)
        for entry in prerequisites:
            adjs[entry[0]].add(entry[1])
        
        gloabl_visited = set()
        ans = []
        cycle_found = False

        def dfs(course_num, local_visited):
            nonlocal cycle_found
            nonlocal gloabl_visited
            nonlocal ans
            
            if course_num in local_visited:
                cycle_found = True
                return 
            
            if course_num in gloabl_visited:
                return
            
            if cycle_found:
                return
            
            local_visited.add(course_num)
            gloabl_visited.add(course_num)

            more_courses = adjs[course_num]
            for course in more_courses:
                dfs(course, local_visited)
            
            local_visited.remove(course_num)
            ans.append(course_num)

        for i in range(numCourses):
            local_visited = set()
            if i not in gloabl_visited:
                dfs(i, local_visited)
        
        return ans if not cycle_found else []


