class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        start_pos = (0,0)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "*":
                    start_pos = (row, col)
        
        queue = collections.deque([(start_pos, 0)])
        visited.add(start_pos)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            (cur_row, cur_col), path_len = queue.popleft()
            if grid[cur_row][cur_col] == "#":
                return path_len
            for direction in directions:
                new_row = cur_row + direction[0]
                new_col = cur_col + direction[1]
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != "X" and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append(((new_row, new_col), path_len+1))
        
        return -1
