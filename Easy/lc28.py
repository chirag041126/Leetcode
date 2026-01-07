# Find the index of the First Occurence in a string
class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle)
s=Solution()
print(s.strStr("hello","ll"))  # Output: 2
print(s.strStr("aaaaa","bba"))  # Output: -1