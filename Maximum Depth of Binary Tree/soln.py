    # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def myRecurs(root):

            if root.left == None and root.right == None:
                return 1
            
            elif root.left == None:
                return 1 + myRecurs(root.right)
            elif root.right == None:
                return 1 + myRecurs(root.left)
            else:
                return 1 + max(myRecurs(root.left), myRecurs(root.right)) 
            
        if root == None:
            return 0
        else:
            return myRecurs(root)