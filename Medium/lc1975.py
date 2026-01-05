# Maximum Matrix Sum
class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        sum1=0
        negetive=0
        min_val = float('inf')
        for i in matrix:
            for j in i:
                if j<0:
                    negetive+=1
                sum1 += abs(j) 
                min_val = min(min_val, abs(j))
        if negetive%2==0:
            return sum1
        else:
            return sum1-(2 * min_val)
s=Solution()
print(s.maxMatrixSum([[1, -1, 1], [-1, -1, -1], [1, -1, 1]]))  # Output: 8  
print(s.maxMatrixSum([[5, -7, 3], [-4, -2, 6], [8, -1, -9]]))  # Output: 40
        