class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0 :
            return nums1
        
        else : 
            j = 0
            for i in range(len(nums1)):
                if m <= 0:
                    nums1[i] = nums2[j]
                    if j + 1 < n: 
                        j += 1
                
                elif nums1[i] > nums2[j]:
                    temp = nums1[i]
                    nums1[i] = nums2[j]
                    nums2[j] = temp
                
                m -= 1
                    
                nums2 = sorted(nums2)