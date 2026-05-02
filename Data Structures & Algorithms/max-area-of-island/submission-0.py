class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j):
            if grid[i][j] != 1:
                return 0

            grid[i][j] = 0
            area = 1

            for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                r = i + dr
                c = j + dc

                if 0 <= r < m and 0 <= c < n:
                    area += dfs(r,c)

            return area

        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                   max_area = max(max_area,dfs(i,j))

        return max_area
        
