# Length of last word
class Solution(object):
    def lengthOfLastWord(self, s):
        y=s.split()
        return len(y[-1])
s=Solution()
print(s.lengthOfLastWord("Hello World"))  # Output: 5
print(s.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(s.lengthOfLastWord("luffy is still joyboy"))  # Output: 6