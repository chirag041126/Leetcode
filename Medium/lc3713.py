class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n, ans = len(s), 0
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1
                non_zero = [f for f in freq if f > 0]
                if non_zero:
                    if min(non_zero) == max(non_zero):
                        ans = max(ans, j - i + 1)
        return ans
s=Solution()
print(s.longestBalanced("abbac"))
#output : 4