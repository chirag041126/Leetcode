# Keep Multiplying Found Values by Two
class Solution(object):
    def findFinalValue(self, nums, original):
        while original in nums:
            original=original*2
        return original            
s=Solution()
print(s.findFinalValue([5,3,6,1,12],3))  # Output: 24
print(s.findFinalValue([2,7,9],4))        # Output: 4