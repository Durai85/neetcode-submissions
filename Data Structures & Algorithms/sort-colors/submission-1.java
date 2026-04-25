class Solution {
    public void sortColors(int[] nums) {
        mergeSort(nums,0,nums.length-1);
    }

    private void mergeSort(int[] nums, int left, int right){
        if(left < right){
            int mid = left + (right - left) / 2;
            mergeSort(nums, left, mid);
            mergeSort(nums, mid+1, right);
            merge(nums, left, mid, right);
        }
    }

    private void merge(int[] nums, int left, int mid, int right){
        int n1 = mid - left + 1;
        int n2 = right - mid;
        
        int leftHalf[] =  new int[n1];
        int rightHalf[] = new int[n2];

        for(int i=0; i<n1; i++) leftHalf[i] = nums[i + left];
        for(int i=0; i<n2; i++) rightHalf[i] = nums[mid + i + 1];

        int i=0, j=0, k=left;
        while(i<n1 && j<n2){
            if(leftHalf[i] <= rightHalf[j]){
                nums[k++] = leftHalf[i++];
            }
            else{
                nums[k++] = rightHalf[j++];
            }
        }

        while(i<n1){
            nums[k++] = leftHalf[i++];
        }

        while(j<n2){
            nums[k++] = rightHalf[j++];
        }
    }
}