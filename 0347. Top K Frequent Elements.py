from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        count_list = [(-1 * counter[entry], entry) for entry in counter]
        heapq.heapify(count_list)
        ans = []
        for i in range(k):
            ans.append(count_list[0][1])
            heapq.heappop(count_list)
        return ans
