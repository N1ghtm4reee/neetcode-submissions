class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> _m;
        map<char, int> _m2;
        for (int i = 0; i < s.size(); i++) {
            _m[s[i]]++;
        }
        for (int j = 0; j < t.size(); j++) {
            _m2[t[j]]++;
        }
        return (_m == _m2);
    }
};
