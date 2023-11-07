# Leetcode Problem
def romanToInt(s):
    equiv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    skip = False
    for i in range(0, len(s)):
        if not(skip):
            if i != len(s) - 1:
                if equiv[s[i]] >= equiv[s[i+1]]:
                    number += equiv[s[i]]
                    skip = False
                else:
                    number += equiv[s[i+1]] - equiv[s[i]]
                    skip = True
            else:
                number += equiv[s[i]]
        else:
            skip = False
    return number


print(romanToInt('MCMXCIV'))