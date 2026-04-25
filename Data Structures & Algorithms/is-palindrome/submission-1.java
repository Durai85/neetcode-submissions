class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        s = s.toLowerCase();
        while (left < right){
            char l = s.charAt(left);
            char r = s.charAt(right);
            if(Character.isLetterOrDigit(l) && Character.isLetterOrDigit(r)){
                if(l!=r) return false;
                left++;
                right--;
            }
            if(!Character.isLetterOrDigit(l)) left++;
            if(!Character.isLetterOrDigit(r)) right--;
        }
        return true;
    }
}
