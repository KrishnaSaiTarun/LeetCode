# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    # While going up, either you are includeing the node or you are not 
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def find_depth(node) -> int:
            nonlocal result 
        
            if not node:
                return 0
            
            left_depth = find_depth(node.left)
            right_depth = find_depth(node.right)

            result = max(result, left_depth+right_depth)
            return max(left_depth, right_depth) + 1
        
        find_depth(root)
        return result
