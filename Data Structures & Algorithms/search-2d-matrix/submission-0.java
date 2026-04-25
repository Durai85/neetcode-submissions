class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int n = matrix[0].length;
        for(int mat[] : matrix){
            if(mat[0] <= target && target <= mat[n-1]){
                int left = 0;
                int right = n-1;
                while(left <= right){
                    int mid = left + (right - left) / 2;
                    if(mat[mid] == target) return true;
                    else if(mat[mid] < target) left = mid + 1;
                    else right = mid - 1;
                }
            }
        }
        return false;
    }
}
