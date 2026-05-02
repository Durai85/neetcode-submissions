class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        q = deque()
        for i in range(1,n-1):
            if board[0][i] == 'O':
                q.append((0,i))
            if board[m-1][i] == 'O':
                q.append((m-1,i))

        for j in range(m):
            if board[j][0] == 'O':
                q.append((j,0))
            if board[j][n-1] == 'O':
                q.append((j,n-1))

        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                board[i][j] = 'S'
                for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                    r, c = i + dr, j + dc
                    if 0 <= r < m and 0 <= c < n and board[r][c]=='O':
                        q.append((r,c))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        

