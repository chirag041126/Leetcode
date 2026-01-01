# Word Pattern
class Solution(object):
    def wordPattern(self, pattern, s):
        s=s.split()
        if len(pattern)!=len(s):
            return False

        mp = {}
        for i in range(len(pattern)):
            if pattern[i] in mp:
                if mp[pattern[i]] != s[i]:
                    return False
            else:
                mp[pattern[i]] = s[i]

        if len(set(mp.values())) != len(mp):
            return False

        return True
s=Solution()
print(s.wordPattern("abba", "dog cat cat dog"))  # Output: true
print(s.wordPattern("abba", "dog cat cat fish")) # Output: false
print(s.wordPattern("aaaa", "dog cat cat dog")) # Output: false
print(s.wordPattern("abba", "dog dog dog dog")) # Output: false
        