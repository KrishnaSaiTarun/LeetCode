from collections import defaultdict

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Lets use stone num = index of stone 

        adj = defaultdict(list)
        for stone in stones:
            x = stone[0] + 1
            y = -1 * (stone[1] + 1)
            adj[x].append(y)
            adj[y].append(x)
        
        visited = set()
        connected_graphs = 0

        def dfs(row_col):
            nonlocal visited
            nonlocal adj
            visited.add(row_col)
            for point in  adj.get(row_col, []):
                if point not in visited:
                    dfs(point)
    

        for row_col in adj.keys():
            if row_col not in visited:
                dfs(row_col)
                connected_graphs += 1

        return len(stones) - connected_graphs
