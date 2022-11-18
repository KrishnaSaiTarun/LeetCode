class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if len(grid) == 0:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == "0":
                return 
            
            grid[i][j] = "0"
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
            return 

        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i,j)
                    ans += 1
        return ans
