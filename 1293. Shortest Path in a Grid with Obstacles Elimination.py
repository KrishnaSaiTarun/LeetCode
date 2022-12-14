class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        rows, cols = len(grid), len(grid[0])

        if k >= rows - 1 + cols -1:
            return rows + cols - 2
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        queue = collections.deque([(0, 0, k, 0)])

        visited = set([(0, 0, k)])

        while queue:

            x, y, remaining_k, path = queue.popleft()

            if (x, y) == (rows-1, cols-1):
                return path 
            
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]

                if (0 <= new_x < rows) and (0 <= new_y < cols):
                    new_k = remaining_k - grid[new_x][new_y]
                    
                    if new_k >= 0 and (new_x, new_y, new_k) not in visited:
                        visited.add((new_x, new_y, new_k))
                        queue.append((new_x, new_y, new_k, path+1))
            
        return -1
