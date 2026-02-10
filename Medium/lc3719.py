class Solution:
    def longestBalanced(self, nums):
        n = len(nums)
        res = 0
        seen = [0] * (max(nums) + 1)

        for i in range(n):
            cnt = [0, 0] 
            for j in range(i, n):
                val = nums[j]
                if seen[val] != i + 1:
                    seen[val] = i + 1
                    cnt[val & 1] += 1
                if cnt[0] == cnt[1]:
                    res = max(res, j - i + 1)
        return res
s=Solution()
print(s.longestBalanced([2,5,4,3]))
# output has : 4