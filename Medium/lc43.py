# Multiply String
class Solution(object):
    def multiply(self, num1, num2):
        num=int(num1)*int(num2)
        return str(num)
s=Solution()
print(s.multiply("123","456"))
# Output: "56088"