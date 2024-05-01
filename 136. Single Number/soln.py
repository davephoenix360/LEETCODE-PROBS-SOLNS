# Solution Idea from Krypto2_0
# https://leetcode.com/problems/single-number/solutions/1771720/c-easy-solutions-sorting-xor-maps-or-frequency-array/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_ans = 0
        
        for i in nums:
            my_ans ^= i
        
        return my_ans
         


mySolu = Solution()
nums = [1,4,2,1,2]
print(mySolu.singleNumber(nums))