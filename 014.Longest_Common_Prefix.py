
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key = len)

        results = []
        max_prefix = strs[0]
        for i in strs:
            prefix = ""
            for j in range(len(max_prefix)):
                if i[j] != max_prefix[j]:
                    break
                prefix += i[j]
            results.append(prefix)
        if not results:
            return ""        
        return min(results)

            