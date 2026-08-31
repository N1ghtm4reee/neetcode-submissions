class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> _map;
        int count = 0;
        int highest = 0;
        for (int i = 0; i < s.size(); i++) {
            if (_map.find(s[i]) != _map.end()) {
                i = _map[s[i]];
                _map.clear();
                count = 0;
            }
            else {
                _map[s[i]] = i;
                count++;
            }
            highest = max(highest, count);
        }
        return highest;
    }
};
