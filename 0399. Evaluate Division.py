from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(defaultdict)

        for (divident, divisor), value in zip(equations, values):
            graph[divident][divisor] = value
            graph[divisor][divident] = 1/value
        
        def find_ans(divident, divisor, seen, prod) -> int:
            seen.add(divident)
            ret = -1
            neighbors = graph[divident]
            if divisor in neighbors:
                return prod * neighbors[divisor]
            for neighbor, val in neighbors.items():
                if neighbor in seen:
                    continue
                ret = find_ans(neighbor, divisor, seen, prod*val)
                if ret != -1:
                    break   
            seen.remove(divident)
            return ret 
            

            
        ans = []
        for divident, divisor in queries:
            if divident not in graph or divisor not in graph:
                ans.append(-1)
            elif divident == divisor:
                ans.append(1)
            else:
                seen = set()
                ans.append(find_ans(divident, divisor, seen, 1))
        
        return ans 
