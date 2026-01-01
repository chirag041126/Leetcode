# Remove Element
class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
s=Solution()
print(s.removeElement([3,2,2,3],3))  # Output: 2
print(s.removeElement([0,1,2,2,3,0,4,2],2))  # Output: 5
print(s.removeElement([0,1,2,3,4,5],6))  # Output: 6