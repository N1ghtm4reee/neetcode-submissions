class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::map<int,int> _map;
        for (auto i = 0; i < nums.size(); i++) {
            if (auto val = _map.find(nums[i]); val != _map.end())
                return true;
            _map[nums[i]] = 1;
        }
        return false;
    }
};