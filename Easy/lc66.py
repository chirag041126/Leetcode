# Plus One
class Solution(object):
    def plusOne(self, digits):
        a=""
        for i in digits:
            a=a+str(i)
        a=int(a)    
        out=str(a+1)
        l=[]
        for i in out:
            l.append(int(i))
        return l
s=Solution()
print(s.plusOne([1,2,3]))  # Output: [1, 2, 4]
print(s.plusOne([4,3,2,1]))  # Output: [4, 3, 2, 2]
print(s.plusOne([9]))  # Output: [1, 0]