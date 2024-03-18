"""
AUTHOR: THE PHOENIX CODER
"""

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        sign = 'positive'
        s = s.strip()
        if s == "":
            return 0
        if (s[0] == '-' or s[0] == '+') or (s[0] >= '0' and s[0] <= '9'):
            if s[0] == '-':
                sign = 'negative'
            
            start = 0 if (s[0] >= '0' and s[0] <= '9') else 1
            for i in range(start, len(s)):
                if not(s[i] >= '0' and s[i] <= '9'):
                    break;
                ans = ans*10+int(s[i])
                if ans >= 2147483648 and sign == 'negative':
                    ans = 2147483648
                    break    
                elif ans >= 2147483647:
                    ans = 2147483647
                    break
        
        if sign == 'negative':
            return ans*-1
        return ans


mySoln = Solution()
print(mySoln.myAtoi(".1"))