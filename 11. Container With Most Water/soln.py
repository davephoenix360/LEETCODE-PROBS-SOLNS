"""
AUTHOR: THE PHOENIX CODER
Solution info: Runtime = 541ms, Memory = 22.23MB
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        maxArea = 0
        while left != right:
            area = min(height[left], height[right])*(right-left)
            maxArea = area if(area > maxArea) else maxArea
            if height[left] > height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                if height[left+1] > height[left]:
                    left += 1
                else:
                    right -= 1
        
        return maxArea
                    
mySolu = Solution()
print(mySolu.maxArea([2,5,4]))