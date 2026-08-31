class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // we need to store each elemet in the array as a key=value and value=index
        std::map<int,int> _map;
        for (int i = 0; i < nums.size(); i++) {
            auto it = _map.find(target - nums[i]);
            if ( it != _map.end()) {
                return {_map[target - nums[i]], i};
            }
            _map[nums[i]] = i;
        }
        return {};
    }
};
