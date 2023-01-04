from collections import defaultdict
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks_count = defaultdict(int)
        for task in tasks:
            tasks_count[task] += 1
        
        already_calculated = {}
        
        def get_best_count(num) -> int:
            nonlocal already_calculated
            count = 0
            if num == 4:
                count = 2
            if num % 3 == 0:
                count = num // 3
            elif num % 3 == 2:
                count = num//3 + 1
            elif num % 3 == 1 and num != 4:
                count = 2 + (num-4)//3

            already_calculated[num] = count
            return count

        rounds = 0
        for num in tasks_count.values():
            if num == 1:
                return -1 
            if num in already_calculated:
                rounds+=already_calculated[num]
            else:
                rounds += get_best_count(num)

        return rounds 
