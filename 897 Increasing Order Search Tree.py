# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        vals = []
        def inord(node):
            if not node:
                return
            inord(node.left)
            vals.append(node.val)
            inord(node.right)
            
        inord(root)
        tree = TreeNode(val=vals[0])
        tmp = tree
        for i in vals[1:]:
            tmp.right = TreeNode(val=i)
            tmp = tmp.right
            
        return tree