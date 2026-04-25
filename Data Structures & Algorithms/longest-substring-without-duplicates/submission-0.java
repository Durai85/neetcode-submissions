class Solution {
    public int lengthOfLongestSubstring(String s) {
        int count = 0;
        Set<Character> seen = new HashSet<>();
        int left = 0, right = 0;
        while (right < s.length()){
            if(!seen.contains(s.charAt(right))){
                seen.add(s.charAt(right++));
            }
            else{
                seen.remove(s.charAt(left++));
            }
            
            count = Math.max(count, seen.size());
        }
        return count;
    }
}
