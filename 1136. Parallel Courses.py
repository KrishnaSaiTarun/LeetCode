from typing import List 

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        # indegree_count = {i:0 for i in range(1, n+1)}
        adj = {i:[] for i in range(1, n+1)}

        for prevCourse, nextCourse in relations:
            adj[prevCourse].append(nextCourse)
            # indegree_count[nextCourse] += 1

        # def get_root_nodes() -> List[int]:
        #     return [node for node, count in indegree_count.items() if count == 0]

        # root_nodes = get_root_nodes()
        
        globally_visited = {}
        locally_visited = set()
        def do_dfs(node) -> int:
            nonlocal adj 
            if node in globally_visited:
                return globally_visited[node]

            if node in locally_visited:
                return -1 
                
            locally_visited.add(node)
            path = 1
            for neighbor in adj[node]:
                new_path = do_dfs(neighbor)
                if new_path == -1:
                    return -1 
                path = max(new_path + 1, path)
            locally_visited.remove(node)
            globally_visited[node] = path
            return path 

        path_len = 0
        for node in range(1,n+1):
            new_path_len = do_dfs(node)
            if new_path_len == -1:
                return -1 
            path_len = max(new_path_len, path_len)
        
        return path_len
