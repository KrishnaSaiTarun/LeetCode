import math
import heapq

class Solution:
    def distance(self, x,y):
        return math.sqrt((x ** 2) + (y ** 2))
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_heap = [(self.distance(point[0], point[1]) , point[0], point[1]) for point in points]
        heapq.heapify(distance_heap)
        ans = []
        for i in range (k):
            ans.append((distance_heap[0][1], distance_heap[0][2])) 
            heapq.heappop(distance_heap)
        return ans 
