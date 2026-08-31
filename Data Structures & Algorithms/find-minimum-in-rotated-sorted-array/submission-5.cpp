class Solution {
public:
    int findMin(vector<int> &nums) {
        int l = 0;
        int r = nums.size() - 1;
        int min = nums[0];
        while(l <= r)
        {
            int m = (l + r) / 2;
            if (nums[m] < min)
                min = nums[m];
            if (nums[m] > nums[r])
            {
                l = m + 1;
                if (nums[l] < min)
                    min = nums[l];
            }
            else if (nums[m] < nums[l])
            {
                r = m - 1;
                if (nums[r] < min)
                    min = nums[r];
            }
            else
                break;
        }
        return min;
    }
};
