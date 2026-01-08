# Max Dot Product of Two Subsequences
class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n=len(nums1)
        m=len(nums2)
        dp=[[float('-inf')] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                product=nums1[i]*nums2[j]

                if i>0 and j>0:
                    product+=max(0,dp[i-1][j-1])
                current_max = product
                if i>0:
                    current_max=max(current_max,dp[i-1][j])
                if j>0:
                    current_max = max(current_max,dp[i][j-1])
                dp[i][j]=current_max
        return dp[n-1][m-1]
s=Solution()
print(s.maxDotProduct([2,1,-2,5], [3,0,-6]))  # Output: 18
print(s.maxDotProduct([-1,-1], [1,1]))  # Output: -1