class Solution:
    def climbStairs(self, n: int) -> int:
        dic = {}

        def steps(n):
            if n == 1:
                return 1
            if n == 2:
                return 2

            if n in dic:
                return dic[n]
            
            dic[n] = steps(n-1) + steps(n-2)

            return dic[n]

        return steps(n)