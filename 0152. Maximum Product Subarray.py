class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        ans = nums[0]
        for num in nums[1:]:
            temp_max_so_far = max(max_so_far*num , num, min_so_far*num)
            min_so_far = min(max_so_far*num , num, min_so_far*num)
            ans = max(ans, temp_max_so_far)
            max_so_far = temp_max_so_far
        return ans
