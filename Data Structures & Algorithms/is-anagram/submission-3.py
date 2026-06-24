class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arr = [0] * 26
        for i in range(len(s)):
            c1 = ord(s[i]) - ord('a')
            c2 = ord(t[i]) - ord('a')
            arr[c1] += 1
            arr[c2] -= 1

        for i in arr:
            if i != 0:
                return False

        return True
        