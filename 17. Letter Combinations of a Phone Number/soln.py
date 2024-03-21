"""
AUTHOR: THE PHOENIX CODER
Runtime: 12ms ( Beats 74.03% )
Memory: 11.71mb ( Beats 40.67% )
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        result = []
        for i in range(len(digits)):
            num = digits[0]
            digits = digits[1:]
            if len(result) == 0:
                result = mapping[num]
            else:
                temp = []
                for letter in mapping[num]:
                    temp += [x+letter for x in result]
                result = temp
        
        return result
        
        
mySolu = Solution()
print(mySolu.letterCombinations(""))
