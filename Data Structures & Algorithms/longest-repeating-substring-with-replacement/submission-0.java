class Solution {
    public int characterReplacement(String s, int k) {
        int left = 0;
        int max  = 0;
        int result = 0;
        int[] map = new int[26];

        for(int right = 0; right < s.length(); right++){
            char r = s.charAt(right);
            map[r - 'A']++;
            max = Math.max(max, map[r - 'A']);
            if(right - left + 1 - max > k){
                char l = s.charAt(left++);
                map[l - 'A'] --;
            }
            result = Math.max(result, right - left + 1);
        }
        return result;
    }
}
