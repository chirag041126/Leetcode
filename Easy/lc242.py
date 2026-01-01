# Valid Anagram
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
s=Solution()
print(s.isAnagram("anagram", "nagaram"))  # Output: true
print(s.isAnagram("rat", "car"))          # Output: false