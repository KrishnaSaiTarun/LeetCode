class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x:x[0])
        arrows = 1
        cur_overlap_ending = points[0][1]
        for point in points[1:]:
            if point[0] > cur_overlap_ending:
                arrows+=1
                cur_overlap_ending = point[1]
            else:
                cur_overlap_ending = min(cur_overlap_ending, point[1])
        
        return arrows
