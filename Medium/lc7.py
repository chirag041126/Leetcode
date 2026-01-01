class Solution(object):
    def reverse(self, x):
        s=str(x)
        if x>=0:
            output=s[::-1]
            if int(output) > 2**31 - 1:
                return 0
            return int(output)
        elif x<0:
            s=s[1:]
            output=s[::-1]
            if int(output) > 2**31 - 1:
                return 0
            return (-1)*int(output)
s=Solution()
print(s.reverse(-123))

       
        