# Valid Pallindrome
class Solution(object):
    def isPalindrome(self,s):
        y=""
        for i in s:
           if i.isalnum():
                y=y+i
        y=y.lower()        
        return y==y[::-1]                
s=Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))  # Output: true
print(s.isPalindrome("race a car")) # Output: false