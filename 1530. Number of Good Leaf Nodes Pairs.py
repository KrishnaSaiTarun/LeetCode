# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        """
        KST:
        At every node, we need to know 
        1. Distance to leaves
        2. Can I make more good leaves 
        """
        return self.countPairsHelper(root, distance)[1]

    def countPairsHelper(self, root, distance):

        if not root:
            return ([], 0)

        if not root.left and not root.right:
            return ([1], 0)
        
        l_distances, l_pairs = self.countPairsHelper(root.left, distance)
        r_distances, r_pairs = self.countPairsHelper(root.right, distance)
        pairs = l_pairs + r_pairs
        for el in l_distances:
            for er in r_distances:
                if el + er <= distance:
                    pairs += 1
                    
        return ([element + 1 for element in l_distances + r_distances if element + 1 < distance], pairs)
