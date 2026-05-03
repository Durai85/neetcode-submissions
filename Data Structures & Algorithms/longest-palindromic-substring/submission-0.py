class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]

        start, end = 0, 0

        for i in range(n):
            dp[i][i] = True

        for i in range(n-1):
            dp[i][i+1] = s[i] == s[i+1]
            if dp[i][i+1] and 2 > end - start + 1:
                start, end = i, i+1

        for length in range(3,n+1):
            for i in range(n-length+1):
                j = i + length - 1
                dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                if dp[i][j] and length > end - start + 1:
                    start, end = i, j

        return s[start:end+1]