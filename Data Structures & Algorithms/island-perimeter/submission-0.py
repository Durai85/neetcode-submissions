class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total_perimeter = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total_perimeter += 4
                    for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                        r = i + dr
                        c = j + dc
                        if 0<=r<m and 0<=c<n and grid[r][c] == 1:
                            total_perimeter -= 1

        return total_perimeter