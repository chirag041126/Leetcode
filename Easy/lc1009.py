class Solution(object):
    def bitwiseComplement(self, n):
        
        if n == 0:
            return 1

        binary = ""

        while n > 0:
            remainder = n % 2
            binary = str(remainder) + binary
            n = n // 2

        x = ""
        for i in binary:
            if i == "0":
                x = x + "1"
            else:
                x = x + "0"

        decimal = 0
        power = 0

        for digit in reversed(x):
            decimal += int(digit) * (2 ** power)
            power += 1
        
        return decimal
s = Solution()
print(s.bitwiseComplement(5))