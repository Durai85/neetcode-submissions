class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        
        p = set()
        a = set()
        pq = deque()
        aq = deque()
        for i in range(n):
            p.add((0,i))
            pq.append((0,i))
            a.add((m-1,i))
            aq.append((m-1,i))
        for j in range(m):
            p.add((j,0))
            pq.append((j,0))
            a.add((j,n-1))
            aq.append((j,n-1))
        


        def bfs(queue, visited):
            while queue:
                for _ in range(len(queue)):
                    i,j = queue.popleft()
                    for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                        r, c = i + dr, j + dc
                        if 0<= r < m and 0<= c < n and heights[i][j] <= heights[r][c] and (r,c) not in visited:
                            queue.append((r,c))
                            visited.add((r,c))
        bfs(pq,p)
        bfs(aq,a)
        res = p.intersection(a)

        return [list(i) for i in res]