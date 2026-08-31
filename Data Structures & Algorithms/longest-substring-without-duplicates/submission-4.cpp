class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0;
        int r = 0;
        int sub = 0;
        int maxSub = 0;
        unordered_map<char, int> _map;
        while(r < s.size())
        {
            if (_map.find(s[r]) != _map.end())
                l = max(l, _map[s[r]] + 1);
            _map[s[r]] = r;
            sub = r - l + 1;
            maxSub = max(maxSub, sub);
            r++;
        }
        return maxSub;
    }
};
