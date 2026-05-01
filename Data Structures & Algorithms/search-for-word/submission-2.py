class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        w = len(word)

        if m == 1 and n == 1:
            return board[0][0] == word

        def dfs(i,j,k):
            if k == w:
                return True

            if board[i][j] == "$" or board[i][j] != word[k]:
                return False

            temp = board[i][j]
            board[i][j] = "$"
            
            for dr,dc  in [(0,1),(1,0),(0,-1),(-1,0)]:
                r = i + dr
                c = j + dc
                if 0 <= r < m and 0 <= c < n:
                    if dfs(r,c,k+1):
                        return True
            
            board[i][j] = temp
            return False

        
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True

        return False