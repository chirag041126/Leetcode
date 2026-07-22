# Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        mp = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in mp:
                return [mp[diff], i]

            mp[nums[i]] = i       
s=Solution()
print(s.twoSum([2,7,11,15],9))  # Output:  [0, 1]
print(s.twoSum([3,2,4],6))  # Output:   [1, 2]
print(s.twoSum([3,3],6))  # Output:     [0, 1]