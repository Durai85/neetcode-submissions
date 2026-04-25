class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int max = 0;
        for(int p : piles){
            max = Math.max(max, p);
        }

        int left = 1;
        int right = max;
        // int min = max;

        while (left <= right){
            int mid = left + (right - left) / 2;
            long k = 0;
            for(int p : piles){
                k += (p + mid -1) / mid;
            }
            if(k <= h){
                right = mid - 1;
            }
            else left = mid + 1;
        }
        return left;
    }
}
