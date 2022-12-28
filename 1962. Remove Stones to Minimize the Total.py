import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        totalstones=sum(piles)
        heap= [-1*p for p in piles]
        heapq.heapify(heap)

        while(k>0):
            k=k-1
            topelement=-1*heapq.heappop(heap)
            remove=topelement//2
            totalstones-=remove
            heapq.heappush(heap,-1*(topelement-remove))
        return totalstones
