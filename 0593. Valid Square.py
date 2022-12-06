class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # conditions:
        # 1. all lens same 
        # 2. points how to do?
        all_points = [p1, p2, p3, p4]
        all_points = sorted(all_points)
        distances = set()
        # p1p2 p1p3 p3p4 p2p4
        distances.add(self.distance(all_points[0], all_points[1]))
        distances.add(self.distance(all_points[0], all_points[2]))
        distances.add(self.distance(all_points[2], all_points[3]))
        distances.add(self.distance(all_points[1], all_points[3]))

        if len(distances) != 1:
            return False 
        
        distances.add(self.distance(all_points[0], all_points[3]))
        distances.add(self.distance(all_points[1], all_points[2]))

        if len(distances) != 2:
            return False 
        
        return True

    
    def distance(self, p1: List[int], p2: List[int]) -> int:
        return (((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)) ** 1/2
