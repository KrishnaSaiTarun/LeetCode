from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        neighbors = defaultdict(list)
        for edge in edges:
            neighbors[edge[0]].append(edge[1])
            neighbors[edge[1]].append(edge[0])
        visited = set()
        def dfs(node):
            visited.add(node)
            res = 0
            for neighbor in neighbors[node]:
                if neighbor not in visited:
                    res+=dfs(neighbor)
            
            if node == 0:
                return res 

            return res+2 if (res > 0 or hasApple[node]) else res
                    
        return dfs(0)
