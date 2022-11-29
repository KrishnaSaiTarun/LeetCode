# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        if not root:
            return q

        q.append(root)
        ans = []
        left_to_right = 1
        while q:
            n = len(q)
            level_list = []
            for i in range(n):
                element = q.pop(0)
                level_list.append(element.val)
                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)
            if left_to_right == 1:
                ans.append(level_list)
            else:
                ans.append(level_list[::-1])
            left_to_right *= -1
        return ans 



