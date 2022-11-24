class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """

        cur_set = set()
        best_ans = 0
        local_ans = 0
        last_occurance_of_cur_seq = -1
        last_val_seen = -1
        for i in range(0, len(fruits)):

            if fruits[i] not in cur_set:
                if len(cur_set) == 2:
                    cur_set.clear()
                    best_ans = max(best_ans, local_ans)
                    cur_set.add(fruits[i])
                    cur_set.add(last_val_seen)
                    local_ans = i - last_occurance_of_cur_seq + 1

                else:
                    cur_set.add(fruits[i])
                    local_ans += 1

                last_occurance_of_cur_seq = i
                last_val_seen = fruits[i]
            
            else:
                local_ans += 1
                if last_val_seen != fruits[i]:
                    last_occurance_of_cur_seq = i
                    last_val_seen = fruits[i]
        
        return max(best_ans, local_ans)



        
        
