class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        r = len(grid)
        c = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >=r or j < 0 or j >=c or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            area = 1
            area += dfs(i, j+1)
            area += dfs(i+1, j)
            area += dfs(i-1, j)
            area += dfs(i, j-1)
            return area

        ans = 0
        for i in range(r):
            for j in range(c):
                ans = max(ans, dfs(i,j))


        return ans
