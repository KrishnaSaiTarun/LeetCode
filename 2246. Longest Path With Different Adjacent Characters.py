from typing import Tuple
from collections import defaultdict
import heapq
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adj_list = defaultdict(list)
        for i in range(1, len(parent)):
            adj_list[parent[i]].append(i)
            adj_list[i].append(parent[i])
        ans = 0
        visited = set()

        def dfs(node) -> Tuple[int, bool]:
            nonlocal ans 
            visited.add(node)
            paths_to_consider = []
            heapq.heapify(paths_to_consider)

            for nei in adj_list[node]:
                path_res = 0
                if nei not in visited:
                    path_res = dfs(nei)
                    if s[nei] != s[node]:
                        heapq.heappush(paths_to_consider, -1 * path_res)
            
            path_through_node = 1
            if not paths_to_consider:
                return path_through_node

            max_path_through_node = -1*paths_to_consider[0]
            if len(paths_to_consider) >= 2:
                path_through_node += (-1* heapq.heappop(paths_to_consider))
                path_through_node += (-1* heapq.heappop(paths_to_consider))
            else:
                path_through_node += (-1* heapq.heappop(paths_to_consider))

            ans = max(ans, path_through_node)
            return max_path_through_node+1

        res_going_above_0 = dfs(0)
        return max(ans, res_going_above_0)
