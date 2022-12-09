from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Should be a connected graph 
        # len visited == len nodes 
        # ALso for a tree -> edges = n-1 

        if len(edges) != n-1:
            return False 

        edges_from_node = [[] for _ in range(n)]
        for edge in edges:
            edges_from_node[edge[0]].append(edge[1])
            edges_from_node[edge[1]].append(edge[0])
        
        stack = deque([0])
        visited_with_parent = {0:-1}

        while stack:
            node = stack.pop()
            for neighbor in edges_from_node[node]:
                if visited_with_parent.get(node) == neighbor:
                    # if neighbor is a parent 
                    continue
                elif visited_with_parent.get(neighbor):
                    # we saw this and its a cycle
                    return False 
                else:
                    # add to seen 
                    visited_with_parent[neighbor] = node
                    stack.append(neighbor)
        
        return len(visited_with_parent) == n
