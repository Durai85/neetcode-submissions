class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, com = [], []

        def dfs(start):
            if len(com) == k:
                res.append(com[:])
                return 

            for i in range(start,n+1):
                com.append(i)
                dfs(i+1)
                com.pop()

        dfs(1)
        return res