# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List 

class Solution:

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        ans = []

        def get_ans(root) -> Optional[int]:
            nonlocal ans 
            if not root:
                return -1
            
            left = get_ans(root.left)
            right = get_ans(root.right)
            level = max(left, right) + 1

            if level >= len(ans):
                ans.append([])
            ans[level].append(root.val)
            return level

        get_ans(root)
        return ans 
