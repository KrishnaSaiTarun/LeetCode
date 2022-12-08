class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search find left pos 
        # binary search find right pos 
        if not nums:
            return [-1, -1]

        def find_left_pos():
            if nums[0] == target:
                return 0
            l = 0
            r = len(nums)-1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    if mid-1 >= l and nums[mid-1] == target:
                        # that means we still have to go left
                        r =  mid - 1
                    else:
                        return mid
                
                elif nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
            return -1 

        def find_right_pos(left_pos):
            if nums[len(nums)-1] == target:
                return len(nums)-1
            l = left_pos
            r = len(nums)-1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    if mid+1 <= r and nums[mid+1] == target:
                        # that means we still have to go left
                        l =  mid + 1
                    else:
                        return mid
                
                elif nums[mid] > target:
                    r = mid - 1 
                elif nums[mid] < target:
                    l = mid + 1
            return -1     

        left = find_left_pos()
        if left == -1:
            return [-1, -1]
        right = find_right_pos(left)
        return [left, right]

                



