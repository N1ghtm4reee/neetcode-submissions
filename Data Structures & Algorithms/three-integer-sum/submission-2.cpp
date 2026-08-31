class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::vector<vector<int>> sol;
        std::sort(nums.begin(), nums.end());
        std::map<vector<int>, bool> sols;
        for (int i = 0; i < nums.size() - 2; i++) {
            for (int j = i + 1; j < nums.size() - 1; j++) {
                for (int k = j + 1; k < nums.size(); k++) {
                    auto it = sols.find({nums[i], nums[j], nums[k]});
                    if ((nums[i] + nums[j] + nums[k]) == 0 && it == sols.end()) {
                    sols[{nums[i], nums[j], nums[k]}] = true;
                    sol.push_back({nums[i], nums[j], nums[k]});
                }
            }
        }
    }
        return sol;
    }
};
