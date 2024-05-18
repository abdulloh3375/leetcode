
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        b = word.find(ch)
        for i in word:
            if i == ch:
                a = word[:b+1]
                a = a[::-1]
            
                return a+word[b+1:]
        if ch not in word:
            return word
        