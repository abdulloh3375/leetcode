
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = []
        for index, char_1 in enumerate(s):
            data = char_1
            for char_2 in s[index + 1::]:
                if char_2 not in data:
                    data += char_2
                else:
                    break
            a.append(len(data))
        if s:
            return max(a)
        else:
            return 0