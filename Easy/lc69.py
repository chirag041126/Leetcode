# Sqrt(x)
class Solution(object):
    def mySqrt(self, x):
       x=x**0.5
       return int(x)
s=Solution()
print(s.mySqrt(4))   # Output: 2
print(s.mySqrt(8))   # Output: 2
print(s.mySqrt(0))   # Output: 0