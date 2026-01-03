class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = [""]

        for d in digits:
            temp = []
            for prev in res:
                for ch in phone[d]:
                    temp.append(prev + ch)
            res = temp

        return res
s=Solution()
print(s.letterCombinations("23"))
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]