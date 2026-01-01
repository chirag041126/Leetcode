# Single Number
class Solution(object):
    def singleNumber(self, nums):
        for num in nums:
            if nums.count(num) == 1:
                return num
s=Solution()
print(s.singleNumber([2,2,1]))          # Output: 1
print(s.singleNumber([4,1,2,1,2]))      # Output: 4
print(s.singleNumber([1]))               # Output: 1    