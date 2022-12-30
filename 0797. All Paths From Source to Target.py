class Solution:

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans : List[List[int]] = []

        def dfs(node, cur_ans):
            if node == len(graph) - 1:
                ans.append(cur_ans.copy())
                return 
            
            for neighbour in graph[node]:
                cur_ans.append(neighbour)
                dfs(neighbour, cur_ans)
                cur_ans.pop()
            return 

        dfs(0, [0])
        return ans 
