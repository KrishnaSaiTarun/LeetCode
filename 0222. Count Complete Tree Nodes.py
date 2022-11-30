# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def get_depth(self, root) -> int:
        d = 0
        while root.left:
            root = root.left
            d += 1
        return d 

    def check_exists(self, index, d, root) -> bool:
        left = 0
        right = (2 ** d) - 1
        for _ in range(d):
            pivot = left + (right - left)//2
            if index <= pivot:
                right = pivot
                root = root.left
            else:
                left = pivot + 1
                root = root.right 
        
        return root != None

    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        d = self.get_depth(root)
        if d == 0:
            return 1

        # last level nodes are 1 to 2 ** d - 1
        left = 1
        right = (2 ** d) - 1
        while left <= right:
            element_idx = left + (right - left)//2
            exists = self.check_exists(element_idx, d, root)
            if exists:
                left = element_idx + 1
            else:
                right = element_idx - 1
        
        return (2 ** d) - 1 + left
