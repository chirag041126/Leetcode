class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        nums = []
        for row in grid:
            for val in row:
                nums.append(val)
        repeat=0
        missing=0
        for i in range(1,(len(grid)**2)+1):
            if nums.count(i)==0:
                missing=i
            if nums.count(i)==2:
                repeat=i
                
        return [repeat,missing]
s=Solution()
print(s.findMissingAndRepeatedValues([[1,3],[2,2]]))