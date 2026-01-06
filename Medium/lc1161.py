# Maximum Level Sum of a Binary Tree
from collections import deque

class Solution(object):
    def maxLevelSum(self, arr):
        l = []
        i = 0
        n = len(arr)

        while True:
            start = 2**i - 1
            end = 2**(i + 1) - 1

            if start >= n:
                break

            c = 0
            for j in range(start, min(end, n)):
                if arr[j] is not None:
                    c += arr[j]

            l.append(c)
            i += 1

        return l.index(max(l)) + 1
s = Solution()
print(s.maxLevelSum([1,7,0,7,-8,None,None])) #output:2