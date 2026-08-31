class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> _map;
        for (int i = 0; i < nums.size(); i++) {
            auto it = _map.find(target - nums[i]);
            if (it != _map.end()) {
                return {it->second, i};
            }
            _map[nums[i]] = i;
        }
        return {};
    }
};