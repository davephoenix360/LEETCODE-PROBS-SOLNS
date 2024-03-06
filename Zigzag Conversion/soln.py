"""
AUTHOR: THE PHOENIX CODER
Solution info: Runtime = 36ms, Memory = 11.91 MB
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ans = ""
        mod_control = 2*(numRows - 1)
        
        if mod_control == 0:
            ans = s
        else:
            for i in range(numRows):
                selector = i
                while(selector < len(s)):
                    ans += s[selector]
                    if i != 0 and i != numRows-1:
                        checker = int(selector/mod_control)*mod_control + (mod_control - selector%mod_control)
                        if checker < len(s):
                            ans += s[checker]
                    selector += mod_control
        
        return ans

mySolu = Solution()
print(mySolu.convert("ADFSDGBDP", 1))