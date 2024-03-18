"""
AUTHOR: THE PHOENIX CODER
Runtime: 992ms ( Beats 86.69% )
Memory: 61.13mb ( Beats 28.67% )
"""


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sorted_points = sorted(points, key=lambda x : x[0])
        arrows = 1
        main_point = sorted_points[0]
        
        for point in sorted_points:
            if point != main_point:
                if ((point[0] >= main_point[0] and point[0] <= main_point[1]) or (point[1] >= main_point[0] and point[1] <= main_point[1])):
                    if point[1] < main_point[1]:
                        main_point[1] = point[1]
                    continue
                else:
                    main_point = point
                    arrows += 1
        
        return arrows
        
        
mySoln = Solution()
print(mySoln.findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))