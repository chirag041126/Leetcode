# Count Negative Numbers in a Sorted Matrix
class Solution(object):
    def countNegatives(self, grid):
        count=0
        for i in grid:
            for j in i:
                if (j<0):
                    count+=1
        return count            
s=Solution()
print(s.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))  # Output: 8
print(s.countNegatives([[3,2],[1,0]]))  # Output: 0
print(s.countNegatives([[1,-1],[-1,-1]]))  # Output: 3