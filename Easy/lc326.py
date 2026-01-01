# Power of Three
class Solution(object):
    def isPowerOfThree(self, n):
        if n==1:
            return True
        a=1
        while a<n:
            a*=3
            if a==n:
                return True
        return False 
s=Solution()
print(s.isPowerOfThree(1))   # Output: true
print(s.isPowerOfThree(27))  # Output: true
print(s.isPowerOfThree(0))   # Output: false