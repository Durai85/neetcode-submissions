class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        # dp = [0] * (n+1)
        # dp[1] = 1
        # dp[2] = 2

        one = 1
        two = 2
        res = 0

        for i in range(3,n+1):
            res = one + two
            one = two
            two = res

        return res