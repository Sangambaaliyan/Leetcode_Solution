# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def m(self,l,r):
        if l is None and r is None:
            return True
        if l is None or r is None:
            return False
        return l.val==r.val and self.m(l.left,r.left) and self.m(l.right,r.right)
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        return self.m(p,q)
        