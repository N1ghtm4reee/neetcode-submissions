class Solution {
public:

    string getKey(string s1) {
        string sorted_s = s1;
        sort(sorted_s.begin(), sorted_s.end());
        return sorted_s;
    }
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        unordered_map<string, vector<string>> _m;

        for (int i = 0; i < strs.size(); i++) {
            _m[getKey(strs[i])].push_back(strs[i]);
        }
        for (auto j = _m.begin(); j != _m.end(); j++) {
            result.push_back(j->second);
        }
        return result;
    }
};
