class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        best_distance = 0
        l = -1
        r = 0
        def compute_best_distance(i, j):
            return int((j-i)/2)

        while r < len(seats):
            if seats[r] == 1:
                if l == -1:
                    best_distance = r
                else:
                    distance = compute_best_distance(l, r)
                    best_distance = max(distance, best_distance)
                l = r
            r+=1 
        if l!= (r-1):
            best_distance = max(best_distance, (r-1)-l)
        
        return best_distance
