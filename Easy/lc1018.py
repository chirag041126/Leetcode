# Binary Prefix Divisible By 5
class Solution(object):
    def prefixesDivBy5(self, nums):
        l=len(nums)
        arr=[]
        out=[]
        num=0
        for i in nums:
            num=num*2+i 
            arr.append(num)
        for i in arr:
            if i%5==0:
                out.append(True)
            else:
                out.append(False)
        return out
s=Solution()
print(s.prefixesDivBy5([0,1,1]))          # Output: [True, False, False]
print(s.prefixesDivBy5([1,1,1]))          # Output: [False, False, False]
                            

