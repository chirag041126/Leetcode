class Solution:
    def minBitwiseArray(self,nums):
        res=[]
        for a in nums:
            b=a+1
            if a==2: # even prime, no answer
                res.append(-1)
            else:
                res.append(a-((b)&(-b))//2) # smallest number
        return res
s=Solution()
print(s.minBitwiseArray([2,3,5,7])) 
# output has : [-1,1,4,3]