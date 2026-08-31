class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        map<vector<int>, bool> sols;
        for (int i = 0; i < nums.size(); i++) {
           int l = i + 1;
           int r = nums.size() - 1;
           
           while(l < r) {
                int ts = nums[i] + nums[l] + nums[r];
                if (ts > 0)
                    r--;
                else if (ts < 0)
                    l++;
                else
                {
                    auto it = sols.find({nums[i], nums[l], nums[r]});
                    if (it == sols.end()) {
                        res.push_back({nums[i], nums[l], nums[r]});
                        sols[{nums[i], nums[l], nums[r]}] = true;
                    }
                    l++;
                }
           } 
        }
        return res;
    }
};
