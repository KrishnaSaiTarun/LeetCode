# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional 
from collections import deque

class Solution:

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def get_LCA(root) -> Optional[TreeNode]:
            if not root:
                return 
            
            if root.val == startValue or root.val == destValue:
                return root

            L = get_LCA(root.left)
            R = get_LCA(root.right)

            if L and R:
                return root 
            return L or R 
        
        lca = get_LCA(root)
        ps = ""
        pd = ""
        stack = deque([(lca, "")])
        while stack:
            node, path = stack.pop()
            if node.val == startValue:
                ps = path 
            if node.val == destValue:
                pd = path 
            
            if node.left:
                stack.append((node.left, path + "L"))
            if node.right:
                stack.append((node.right, path + "R"))
            if ps and pd:
                break  
        
        return "U" * len(ps) + pd
