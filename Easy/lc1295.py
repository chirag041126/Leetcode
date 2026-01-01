# Find Numbers with Even Number of Digits
class Solution(object):
    def findNumbers(self, nums):
        count=0
        for i in nums:
            if len(str(i))%2==0:
                count+=1
        return count                
s=Solution()
print(s.findNumbers([12,345,2,6,7896]))  # Output: 2
print(s.findNumbers([555,901,482,1771]))  # Output: 1
print(s.findNumbers([1,22,333,4444,55555]))  #  Output: 2