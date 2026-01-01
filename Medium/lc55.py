# Jump Game
class Solution(object):
    def canJump(self, nums):
        far = 0   
        for i in range(len(nums)):
            if i > far:
                return False 
            far = max(far, i + nums[i])
        return True     
s=Solution()
print(s.canJump([2,3,1,1,4]))
# Output: True   