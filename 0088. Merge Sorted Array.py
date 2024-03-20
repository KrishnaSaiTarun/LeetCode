import math
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return 
        if m==0:
            first=float("-inf")
        else:
            first=nums1[m-1]
            
        second=nums2[n-1]
        i,j=m-1,n-1

        for k in range(m+n-1,-1,-1): 
            if first>second:
                nums1[k]=first 
                i-=1
                first=nums1[i] if i>=0 else float("-inf")
            elif second>=first:
                nums1[k]=second
                j=j-1
                second = nums2[j] if j>=0 else float("-inf")
