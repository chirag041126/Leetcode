# Integer to Roman
class Solution(object):
    def intToRoman(self, num):
        l1 = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        l2 = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        i=0
        ans=""
        while num>0:
            for j in range(num//l1[i]):
                ans=ans+l2[i]
                num=num-l1[i]
            i=i+1
        return ans       
s=Solution()
print(s.intToRoman(1994))
# Output: "MCMXCIV"