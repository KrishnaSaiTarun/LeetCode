class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        dp = {}

        def dfs(index, k) -> int:

            if k == 1:
                return sum(nums[index:])
            if (index, k) in dp:
                return dp[(index,k)]
            
            min_val , cur_sum = float("inf"), 0
            for i in range(index, len(nums) - k + 1):
                cur_sum += nums[i]
                max_sum = max(cur_sum, dfs(i + 1, k -1))
                min_val = min(min_val, max_sum)
                if cur_sum > min_val:
                    break
            
            dp[(index, k)] = min_val
            return min_val
        
        return dfs(0, k)
