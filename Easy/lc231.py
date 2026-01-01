# Power of Two
class Solution(object):
    def isPowerOfTwo(self, n):
        if n==1:
            return True
        a=1
        while a<n:
            a*=2
            if a==n:
                return True
        return False 
s=Solution()
print(s.isPowerOfTwo(1))   # Output: true
print(s.isPowerOfTwo(16))  # Output: true
print(s.isPowerOfTwo(3))   # Output: false
        