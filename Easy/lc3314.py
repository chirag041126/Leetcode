class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        max_int=999
        for i in range(len(nums)):
            visited=False
            for j in range(1,max_int):
                if (j | (j+1) ) == nums[i]:
                    visited=True
                    result.append(j)
                    break
            if visited==False:
                result.append(-1)
        return result
s=Solution()
print(s.minBitwiseArray([2,3,5]))  # Output: [1, -1, 4]