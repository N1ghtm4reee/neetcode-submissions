class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() == 0) return 0;
        int maxLen = 1;
        int l = 0, r = 1;
        // map<char, index> to stor chars? and on each it we check the existence of the char
        Map<Character, Integer> subString = new HashMap<>();
        subString.put(s.charAt(l), l);
        while(r < s.length()) {
            while (subString.containsKey(s.charAt(r))) {
                // dup exist, we need to move to dup + 1 index
                subString.remove(s.charAt(l));
                l++;
            }
            subString.put(s.charAt(r), r);
            maxLen = Math.max((r - l) + 1, maxLen);
            r++;
        }
        return maxLen;
    }
}
