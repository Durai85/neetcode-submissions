class Solution {
    public int[] sortArray(int[] nums) {
        mergeSort(nums, 0, nums.length-1);
        return nums;
    }
    private void mergeSort(int[] nums, int left, int right){
        if(left < right){
            int mid = left + (right - left)/2;
            mergeSort(nums, left, mid);
            mergeSort(nums, mid+1, right);
            merge(nums, left, mid, right);
        }
    }
    private void merge(int[] nums, int left, int mid, int right){
        int n1 = mid - left + 1;
        int n2 = right - mid;
        int[] first = new int[n1];
        int[] second = new int[n2];
        for(int i=0; i<n1; i++) first[i] = nums[i + left];
        for(int i=0; i<n2; i++) second[i] = nums[mid + i + 1];
        
        int i=0,j=0,k=left;
        while(i<n1 && j<n2){
            if(first[i] < second[j]){
                nums[k++] = first[i++];
            }
            else{
                nums[k++] = second[j++];
            }
        }
        while(i<n1){
            nums[k++] = first[i++];
        }
        while(j<n2){
            nums[k++] = second[j++];
        }
    }
}