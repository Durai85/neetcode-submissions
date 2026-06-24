class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        i = 0
        j = 0
        n1 = len(word1)
        n2 = len(word2)
        while i < n1 and j < n2:
            result += word1[i]
            result += word2[j]
            i += 1
            j += 1

        if i < n1:
            result += word1[i:]

        if j < n2:
            result += word2[j:]

        return result