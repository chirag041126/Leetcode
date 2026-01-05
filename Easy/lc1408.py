# String Matching in an Array
class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        l=[]
        for i in words:
            for j in range(0,len(words)):
                if i!=words[j%len(words)]:
                    if i in words[j]:
                        l.append(i)
                        break
        return l
s=Solution()
print(s.stringMatching(["mass","as","hero","superhero"]))  # Output: ["as","hero"]
print(s.stringMatching(["leetcode","et","code"]))  # Output: ["et","code"]
print(s.stringMatching(["blue","green","bu"]))  # Output: []    
        