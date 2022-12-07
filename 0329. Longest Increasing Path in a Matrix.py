class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # maintain cur path seen indices 
        # miantain best path from each index so that we can add it to the seen list 

        if not matrix or not matrix[0]:
            return 0

        dp ={}
        ans = 0

        def dfs(i, j):
            nonlocal dp 
            if (i, j) in dp:
                return dp[(i, j)]
            
            down = up = right = left = 1
            if i + 1 < len(matrix) and matrix[i+1][j] > matrix[i][j]:
                down += dfs(i+1, j)
            if j + 1 < len(matrix[0]) and matrix[i][j+1] > matrix[i][j]:
                right += dfs(i, j+1)
            if i - 1 >= 0 and matrix[i-1][j] > matrix[i][j]:
                up += dfs(i-1, j)
            if j - 1 >= 0 and matrix[i][j-1] > matrix[i][j]:
                left += dfs(i, j-1)
            
            best = max(down, left, right, up)
            dp[(i, j)] = best
            return best 


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i, j) not in dp:
                    path = dfs(i, j)
                    ans = max(ans, path)
                else:
                    ans = max(ans, dp[(i, j)])
        
        return ans 
            
