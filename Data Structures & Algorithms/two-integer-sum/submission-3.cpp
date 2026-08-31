class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> _m;
        for (int i = 0; i < nums.size(); i++) {
            int missing = target - nums[i];
            if (_m.find(missing) != _m.end()) {
                return {_m[missing], i};
            }
            _m[nums[i]] = i;
        }
        return {};
    }
};
