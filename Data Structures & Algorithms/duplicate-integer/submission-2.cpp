class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int, bool> _map;
        for (int i = 0; i < nums.size(); i++) {
            if (_map.find(nums[i]) == _map.end())
                _map[nums[i]] = true;
            else
                return true;
        }
        return false;
    }
};