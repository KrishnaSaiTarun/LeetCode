class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        finalPos = len(nums) - 1
        farthest = 0
        for i in range(len(nums)):
            max_reachable_point = nums[i] + i
            if max_reachable_point >= finalPos:
                return True 
            farthest = max(farthest, max_reachable_point)
            if i == farthest:
                return False 
            
