from typing import List 

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        components = n
        group_id = [x for x in range(n)]

        def find(x):
            nonlocal group_id
            if group_id[x] != x:
                group_id[x] = find(group_id[x])
            return group_id[x]
        
        def union(a, b):
            nonlocal components
            nonlocal group_id
            group_a, group_b = find(a), find(b)
            
            if group_a != group_b:
                if group_a < group_b:
                    group_id[group_b] = group_a
                elif group_a > group_b:
                    group_id[group_a] = group_b
                components -= 1

        for timestamp, a, b in sorted(logs):
            union(a,b)
            if components == 1:
                return timestamp 
            
        return -1
