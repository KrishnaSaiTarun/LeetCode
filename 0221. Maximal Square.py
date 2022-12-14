class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_len = 0
        cache = {}
        rows, cols = len(matrix), len(matrix[0])

        def helper(r, c):
            nonlocal max_len
            if r >= rows or c >= cols:
                return 0
            
            if (r,c) not in cache:
                diagnoal = helper(r+1, c+1)
                right = helper(r, c+1)
                down = helper(r+1, c)

                cache[(r,c)] = 0
                if matrix[r][c] == "1":
                    cache[(r,c)] = 1 + min(diagnoal, right, down)
                    
            max_len = max(max_len, cache[(r,c)])
            return cache[(r,c)]
        
        helper(0, 0)
        return max_len ** 2
