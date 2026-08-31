class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, bool> _map;
        for (int i = 0; i < nums.size(); i++) {
            if (_map.find(nums[i]) != _map.end()) {
                return true;
            }
            _map[nums[i]] = true;
        }
        return false;
    }
};