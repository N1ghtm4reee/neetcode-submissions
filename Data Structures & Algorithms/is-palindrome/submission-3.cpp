class Solution {
public:
    bool isPalindrome(string s) {
        int r = s.size() - 1;
        for (int i = 0; i < r; i++) {
            while(s[i] && !isalnum(s[i])) i++;
            while(r >= 0 && !isalnum(s[r])) r--;
            if (tolower(s[i]) != tolower(s[r]))   return false;
            r--;
        }
        return true;
    }
};
