class Solution(object):
    def findDisappearedNumbers(self, nums):
        number = set(nums)
        l1 = []
        for i in range(1,len(nums)+1):
            if i not in number:
                l1.append(i)
        return l1 
s=Solution()
print(s.minimumAbsDifference([4,3,2,7,8,2,3,1]))