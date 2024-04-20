class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        twos = int(n/2)
        ones = n - 2*twos
        ways = 0
        
        memo = {}
        
        while twos >= 0:
            if (twos + ones) not in memo:
                memo[twos+ones] = self.factorial(twos + ones)
            if twos not in memo:
                memo[twos] = self.factorial(twos)
            if ones not in memo:
                memo[ones] = self.factorial(ones)
            
            ways += int(memo[ones+twos]/(memo[ones] * memo[twos]))
            
            twos -= 1
            ones += 2
        
        return int(ways)
    
    def factorial(self, num):
        if num == 0 or num == 1:
            return 1
        else:
            return num * self.factorial(num-1)

        
mySolu = Solution()
print(mySolu.climbStairs(3))