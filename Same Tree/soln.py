# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return myCheck(p, q)

def myCheck(p, q):
    if p == None and q == None:
        return True
    elif p == None and q != None:
        return False
    elif p != None and q ==  None:
        return False

    if p.val == q.val:
        return (myCheck(p.left, q.left)) and (myCheck(p.right, q.right))
    else:
        return False