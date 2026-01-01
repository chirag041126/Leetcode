# Missing Number
class Solution(object):
    def missingNumber(self, nums):
        for i in range (1,len(nums)+1):
            if i not in nums:
                 return i
        return 0
s=Solution()
print(s.missingNumber([3,0,1]))        # Output: 2
print(s.missingNumber([0,1]))          # Output: 2
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))  # Output: 8