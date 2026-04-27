class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        com = []

        def dfs(start):
            if len(com) == k:
                res.append(com[:])
                return

            for x in range(start,n+1):
                com.append(x)
                dfs(x+1)
                com.pop()

        dfs(1)
        return res