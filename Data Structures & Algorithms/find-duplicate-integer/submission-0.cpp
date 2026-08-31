class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        std::unordered_set<int> _set;
        for (int i = 0; i < nums.size(); i++){
            if (_set.count(nums[i]))
                return nums[i];
            _set.insert(nums[i]);
        }
        return -1;
    }
};
