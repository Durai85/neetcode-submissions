class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(i, current):
            if len(current) == k:
                result.append(current.copy())
                return

            current.append(i)
            if i <= n:
                dfs(i+1, current)
            current.pop()
            if i <= n:
                dfs(i+1, current)

            return result

        return dfs(1,[]) 