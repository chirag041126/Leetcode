class Solution:
    def constructTransformedArray(self, nums):
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            ans[i] = nums[(i + nums[i]) % n]
        return ans
s=Solution()
print(s.constructTransformedArray([3,-2,1,1]))
#output : [1,1,1,3]