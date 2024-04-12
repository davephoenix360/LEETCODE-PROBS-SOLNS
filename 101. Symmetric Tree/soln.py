# Slowest soltion ever : (

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        cache_left = [root.left]
        cache_right = [root.right]
        
        any_node = not(root.left == None and root.right == None)
        while any_node:
            print([(i.val if i != None else None) for i in cache_left])
            print(list(reversed([(j.val if j != None else None) or None for j in cache_right])))
            
            if [(i.val if i != None else None) for i in cache_left] != list(reversed([(j.val if j != None else None) for j in cache_right])):
                return False
            else:
                temp = []
                for node in cache_left:
                    any_node =False or ((node.left != None or node.right != None) if node != None else False)
                    temp += [node.left if node != None else None]
                    temp += [node.right if node != None else None]
                cache_left = temp
                temp = []
                for node in cache_right:
                    any_node = any_node or ((node.left != None or node.right != None) if node != None else False)
                    temp += [node.left if node != None else None]
                    temp += [node.right if node != None else None]
                cache_right = temp
        
        return True


n1 = TreeNode(3)
n2 = TreeNode(4)
n3 = TreeNode(4)
n4 = TreeNode(3)
n5 = TreeNode(2)
n6 = TreeNode(2)
root = TreeNode(1, n5, n6)

mySolution = Solution()
print(mySolution.isSymmetric(root))

