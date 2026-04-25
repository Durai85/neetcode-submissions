class Solution {
    public boolean isValidSudoku(char[][] board) {
        int n = board.length;
        boolean row[][] = new boolean[n][n];
        boolean col[][] = new boolean[n][n];
        boolean box[][] = new boolean[n][n];

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(board[i][j]!='.'){
                    int num = board[i][j] - '1';
                    int r = i / 3;
                    int c = j / 3;
                    int b = (r)*3 + c;

                    if(row[i][num] || col[j][num] || box[b][num]) return false;
 
                    row[i][num] = true;
                    col[j][num] = true;
                    box[b][num] = true;

                }
            }
        }
        return true;
    }
}
