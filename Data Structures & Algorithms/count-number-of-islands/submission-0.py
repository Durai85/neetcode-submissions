class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j):
            if grid[i][j]!='1':
                return
            grid[i][j] = '0'

            for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                r = i + dr
                c = j + dc
                if 0 <= r < m and 0 <= c < n:
                    dfs(r,c)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j)
                    
        return count