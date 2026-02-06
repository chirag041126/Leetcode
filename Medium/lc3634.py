class Solution:
    def minRemoval(self, nums, k):
        nums.sort()
        n = len(nums)
        ans = n
        j = 0
        
        for i in range(n):
            while j < n and nums[j] <= nums[i] * k:
                j += 1
            ans = min(ans, n - (j - i))
        
        return ans
s=Solution()
print(s.minRemoval([1,2,3,4], 2))
# output has : 1