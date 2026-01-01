# Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        roman = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        total=0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total       
        
s=Solution()
print(s.romanToInt("III"))      # Output: 3
print(s.romanToInt("LVIII"))    # Output: 58
print(s.romanToInt("MCMXCIV"))  # Output: 1994