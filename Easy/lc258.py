# Add Digits
class Solution(object):
    def addDigits(self, num):
        while 9<num:
            s=str(num)
            count=0
            for i in s:
                count+=int(i)
            num=count
        return num               
s=Solution()
print(s.addDigits(38))  # Output: 2
print(s.addDigits(0))   # Output: 0
print(s.addDigits(9))   # Output: 9