# Excel sheet Column Number
class Solution(object):
    def titleToNumber(self, columnTitle):
        result = 0
        for c in columnTitle:
            result=result*26+(ord(c)-ord('A')+1)
        return result    
s=Solution()
print(s.titleToNumber("A"))      # Output: 1
print(s.titleToNumber("AB"))     # Output: 28
print(s.titleToNumber("ZY"))     # Output: 701