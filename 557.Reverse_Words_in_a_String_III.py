
class Solution:
    def reverseWords(self, s: str) -> str:
        o = s.split()
        res = []
        for i in o:
            a = i[::-1]
            res.append(a)
            
            b = " ".join(map(str, res))
        return b