class Solution {
public:
    bool isAnagram(string s, string t) {
        // calculate the frequency of each character in both arrays compare frequency 
        // if any difference return false
        if (s.size() != t.size()) return false;
        int arr1[26] = {-1};
        int arr2[26] = {-1};

        for (int i = 0; i < s.size(); i++) {
            arr1[s[i] - 'a']++;
        }
        for (int i = 0; i < t.size(); i++) {
            arr2[t[i] - 'a']++;
        }
        for (int i = 0; i < s.size(); i++) {
            if (arr1[s[i] - 'a'] != arr2[s[i] - 'a'])
                return false;
        }
        return true;
    }
};
