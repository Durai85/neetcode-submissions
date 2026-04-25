class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        res = ''
        n = len(strs)
        for i in range(len(strs[0])):
            if strs[0][i] == strs[n-1][i]:
                res += strs[0][i]
            else:
                break
        return res