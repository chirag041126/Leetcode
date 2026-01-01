# Happy Number
class Solution(object):
    def isHappy(self, n):
        seen=set()
        while n!=1:
            if n in seen:     
                return False
            seen.add(n)
            s=str(n)
            count=0
            for i in s:
                count+=int(i)**2
            n=count     
        return  True             
s=Solution()
print(s.isHappy(19))  # Output: true
print(s.isHappy(2))   # Output: false
print(s.isHappy(7))   # Output: true
        