class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False]*9 for _ in range(9)]
        col = [[False]*9 for _ in range(9)]
        box = [[False]*9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    r = i // 3
                    c = j // 3
                    b = (r * 3) + c

                    if row[i][num-1] or col[j][num-1] or box[b][num-1]:
                        return False

                    row[i][num-1] = True
                    col[j][num-1] = True
                    box[b][num-1] = True

        return True 