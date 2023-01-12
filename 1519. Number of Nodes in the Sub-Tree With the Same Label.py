from collections import defaultdict 
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        neighbours = defaultdict(list)
        
        for edge in edges:
            neighbours[edge[0]].append(edge[1])
            neighbours[edge[1]].append(edge[0])
        
        visited = set()
        ans = [0 for _ in range(n)]

        def dfs(node):
            visited.add(node)
            values = defaultdict(int)
            for neighbor in neighbours[node]:
                if neighbor not in visited:
                    local_values_dict = dfs(neighbor)
                    for key in local_values_dict.keys():
                        values[key]+=local_values_dict[key]

            values[labels[node]]+=1
            ans[node] = values[labels[node]]
            return values
            
        dfs(0)
        return ans 
