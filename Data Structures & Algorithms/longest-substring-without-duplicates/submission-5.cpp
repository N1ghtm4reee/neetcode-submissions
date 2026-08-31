class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0;
        int maxSub = 0;
        unordered_map<char, int> _map;
        for (int r = 0; r < s.size(); r++)
        {
            if (_map.find(s[r]) != _map.end() && _map[s[r]] >= l)
                l = _map[s[r]] + 1;
            _map[s[r]] = r;
            maxSub = max(maxSub, r - l + 1);
        }
        return maxSub;
    }
};
