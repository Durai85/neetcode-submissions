class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sub = [], []

        def dfs(start):
            if len(sub) == k:
                res.append(sub[:])
                return

            for i in range(start,n+1):
                sub.append(i)
                dfs(i+1)
                sub.pop()

        dfs(1)
        return res
