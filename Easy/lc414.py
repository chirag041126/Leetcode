# Third Maximum Number
class Solution(object):
    def thirdMax(self, nums):
        nums=set(nums)
        if len(nums)<3:
            return max(nums)
        nums.remove(max(nums))   
        nums.remove(max(nums))                
        return max(nums)
s=Solution()
print(s.thirdMax([3,2,1]))          # Output: 1
print(s.thirdMax([1,2]))            # Output: 2
print(s.thirdMax([2,2,3,1]))        # Output: 1