class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
        count = 0
        while q:
            rotten = False
            for _ in range(len(q)):
                i,j = q.popleft()
                for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                    r = i + dr
                    c = j + dc
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r,c))
                        rotten = True

            if rotten:
                count += 1
        
        # print(grid)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return count