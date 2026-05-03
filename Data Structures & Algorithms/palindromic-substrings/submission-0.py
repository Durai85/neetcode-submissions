class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        
        count = 0
        for i in range(n):
            dp[i][i] = True
            count += 1

        for i in range(n-1):
            dp[i][i+1] = s[i] == s[i+1]
            if dp[i][i+1]:
                count += 1

        for length in range(3,n+1):
            for i in range(n-length+1):
                j = i + length - 1
                dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                if dp[i][j]:
                    count += 1

        return count