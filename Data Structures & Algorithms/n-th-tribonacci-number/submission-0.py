class Solution:
    def tribonacci(self, n: int) -> int:
        dic = {}
        def dp(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1

            if n in dic:
                return dic[n]

            dic[n] = dp(n-1) + dp(n-2) + dp(n-3)

            return dic[n]

        return dp(n)