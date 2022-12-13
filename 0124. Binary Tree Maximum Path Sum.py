# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_path_sum = float("-inf")

        def helper(node: Optional[TreeNode]):

            nonlocal max_path_sum

            if not node:
                return float("-inf")
            
            left_path_max = max(0, helper(node.left))
            right_path_max = max(0,helper(node.right))

            max_path_sum = max(max_path_sum, node.val + left_path_max + right_path_max)
            return max(left_path_max, right_path_max) + node.val
        
        helper(root)
        return max_path_sum
