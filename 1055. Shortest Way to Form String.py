from collections import defaultdict
from bisect import bisect_left

class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        source_indexs = defaultdict(list)
        for i, c in enumerate(source):
            source_indexs[c].append(i)

        count = 0
        prev_source_index = 0 #last char found at 
        for char in target:
            if char not in source_indexs:
                return -1 
            index_list = source_indexs[char]
            index_of_next_char_index_in_source = bisect_left(index_list, prev_source_index)
            if index_of_next_char_index_in_source==len(index_list):
                count+=1
                index_of_next_char_index_in_source = 0
            prev_source_index = index_list[index_of_next_char_index_in_source] + 1
        
        return count + 1
