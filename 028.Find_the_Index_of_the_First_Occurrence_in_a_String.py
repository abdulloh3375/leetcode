
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            a = haystack.find(needle)
            return a
        else:
            return -1
            