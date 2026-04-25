class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int left = 0;
        int right = 0;
        for(int w : weights){
            left = Math.max(left, w);
            right += w;
        }

        while (left <= right){
            int mid = left + (right - left) / 2;
            int daysNeeded = 1;
            int currentLoad = 0;
            for(int w : weights){
                if(currentLoad + w > mid){
                    daysNeeded ++;
                    currentLoad = 0;
                }
                currentLoad += w;
            }

            if(daysNeeded <= days){
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }
        return left;
    }
}