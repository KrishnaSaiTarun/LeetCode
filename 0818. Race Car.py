from collections import deque

class Solution:
    def racecar(self, target: int) -> int:

        queue = deque([(0, 1, 0)])

        while queue:
            pos, speed, moves = queue.popleft()
            if pos == target:
                return moves
            queue.append((pos+speed, speed*2, moves+1))

            if (pos + speed > target and speed > 0) or (pos + speed < target and speed < 0):
                speed = -1 if speed > 0 else 1
                queue.append((pos, speed, moves+1))
        
        return -1
