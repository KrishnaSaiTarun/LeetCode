# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    
    
    
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        directions = [(-1,0), (0, 1), (1,0), (0, -1)]
        
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        
        def backtrack(cell, direction):
            nonlocal directions
            nonlocal visited 
            robot.clean()
            visited.add(cell)
            for k in range(4):
                new_dir = (direction + k) % 4
                next_cell = (cell[0] + directions[new_dir][0], cell[1] + directions[new_dir][1])
                if next_cell not in visited and robot.move():
                    backtrack(next_cell, new_dir)
                    # because we did move() in the new dir 
                    go_back()
                robot.turnRight()
        
        backtrack((0,0), 0)
        
