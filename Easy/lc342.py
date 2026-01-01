# Power of Four
class Solution(object):
    def isPowerOfFour(self, n):
        a=1
        while a<n:
            a*=4
        return a==n   
s=Solution()
print(s.isPowerOfFour(16))  # Output: true
print(s.isPowerOfFour(5))   # Output: false
print(s.isPowerOfFour(1))   # Output: true