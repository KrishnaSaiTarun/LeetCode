"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    head = None
    prev = None
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev:
                node.left = self.prev
                self.prev.right = node
            else:
                self.head = node
            self.prev = node
            
            inorder(node.right)
        
        inorder(root)
        self.head.left = self.prev
        self.prev.right = self.head
        return self.head
