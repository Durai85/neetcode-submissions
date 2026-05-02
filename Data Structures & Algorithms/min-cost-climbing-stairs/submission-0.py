class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dic = {}
        def dp(n):
            if n == 0:
                return cost[0]
            if n == 1:
                return cost[1]

            if n in dic:
                return dic[n]

            dic[n] = cost[n] + min(dp(n-1), dp(n-2))

            return dic[n]

        return min(dp(n-1),dp(n-2))
        