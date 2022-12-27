class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        cap_left = [cap - rock for cap,rock in zip(capacity, rocks)]
        
        for i,cap in enumerate(sorted(cap_left)):
            additionalRocks -= cap
            if additionalRocks == 0:
                return i + 1
            if additionalRocks < 0:
                return i 
        if additionalRocks:
            return len(capacity)
