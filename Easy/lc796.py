class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        shift=0
        s1=""
        for i in range(1,len(s)):
            if s==goal:
                return True
                break
            else:
                s1=s[i:]+s[0:i]
                if s1==goal:
                    return True
                    break
        return False
s=Solution()
print(s.rotateString("abcde","cdeab"))  # Output: True
print(s.rotateString("abcde","abced"))  # Output: False
print(s.rotateString("aa","a"))  # Output: False


        