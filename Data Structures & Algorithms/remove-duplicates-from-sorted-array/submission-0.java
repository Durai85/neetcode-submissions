class Solution {
    public int removeDuplicates(int[] nums) {
        int idx = 0;
        int src = 0;
        while(src < nums.length){
            if(nums[idx]!=nums[src]){
                nums[++idx] = nums[src];
            }
            src++;
        }
        return idx+1;
    }
}