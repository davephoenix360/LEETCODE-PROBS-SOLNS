# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root == None:
            return False
        print(root.val)
        if root.left == None and root.right == None:
            return (root.val == targetSum)
        elif root.left == None:
            return self.hasPathSum(root.right, targetSum-root.val)
        elif root.right == None:
            return self.hasPathSum(root.left, targetSum-root.val)
        else:
            return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)