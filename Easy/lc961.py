# N-Repeated Elements in Size 2N Array
class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s1=set()
        for i in nums:
            if i in s1:
                return i
            else:
                s1.add(i)
s=Solution()
print(s.repeatedNTimes([1,2,3,3]))  # Output: 3
print(s.repeatedNTimes([2,1,2,5,3,2]))  # Output: 2
print(s.repeatedNTimes([5,1,5,2,5,3,5,4]))  # Output: 5