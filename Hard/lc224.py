# Basic Calculator
class Solution(object):
    def calculate(self, s):
        stack = []
        result = 0
        sign = 1
        num = 0
        for ch in s:
            if ch.isdigit():
                num=num*10+int(ch)
            elif ch == "+":
                result=result+sign*num
                num=0
                sign=1
            elif ch == '-':
                result += sign * num
                num = 0
                sign = -1
            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif ch == ')':
                result += sign * num
                num = 0
                result *= stack.pop()  
                result += stack.pop()
        return result + sign * num               
s=Solution()
print(s.calculate("(1+(4+5+2)-3)+(6+8)"))  # Output: 23
print(s.calculate("1 + 1"))  # Output: 2
