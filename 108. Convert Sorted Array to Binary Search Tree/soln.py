# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) > 2:
            head = TreeNode(nums[len(nums)/2], self.sortedArrayToBST(nums[:len(nums)/2]), self.sortedArrayToBST(nums[len(nums)/2+1:]))
        elif len(nums) == 2:
            head = TreeNode(nums[1], left=TreeNode(nums[0]))
        else:
            head = TreeNode(nums[0])
            
        return head
        