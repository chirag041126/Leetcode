class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        ans = 0

        while i < j:
            ans = max(ans, nums[i] + nums[j])
            i += 1
            j -= 1

        return ans
s=Solution()
print(s.minPairSum([3,5,2,3]))