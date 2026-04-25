class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int count = 0;
        int left = 0, right = people.length-1;
        while(left <= right){
            if(people[left] + people[right] <= limit){
                count ++;
                left ++;
                right --;
            }
            else{
                count++;
                right --;
            }
        }
        return count;
    }
}