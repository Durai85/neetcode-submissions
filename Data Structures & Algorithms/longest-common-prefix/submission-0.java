class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        if(strs.length < 2) return strs[0];
        StringBuilder res = new StringBuilder();
        String first = strs[0];
        String last = strs[strs.length-1];
        for(int i=0; i<first.length(); i++){
            if(first.charAt(i) == last.charAt(i)){
                res.append(first.charAt(i));
            }
            else break;
        }
        return new String(res);
    }
}