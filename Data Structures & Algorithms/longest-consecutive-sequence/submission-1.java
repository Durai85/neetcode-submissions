class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length==0) return 0;
        Arrays.sort(nums);
        System.out.println(Arrays.toString(nums));
        int max = 0;
        int count = 1;
        for(int i=1; i<nums.length; i++){
            if(nums[i-1]==nums[i]) continue;
            else if(nums[i]-nums[i-1] == 1) count++;
            else{
                max = Math.max(count, max);
                count = 1;
            }
        }   
        return Math.max(count, max);
    }
}
