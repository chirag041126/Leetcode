class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)==1 & len(t)==1:
            return True
        d1={}
        d2={}
        for i in range(len(s)):
            c1=s[i]
            c2=t[i]
            if c1 in d1:
                if d1[c1]!=c2:
                    return False
            else:
                d1[c1]=c2
            if c2 in d2:
                if d2[c2]!=c1:
                    return False
            else:
                d2[c2]=c1
        return True
s=Solution()
print(s.isIsomorphic("egg","add"))

        