class Solution {
public:
    int maxArea(vector<int>& heights) {
        int Max = 0;
        int l = 0;
        int r = heights.size() - 1;
        while(l < r) {
            int d = r - l;
            int h = min(heights[l], heights[r]);
            Max = max(Max, h * d);
            if (heights[l] < heights[r])
                l++;
            else
                r--;
        }
        return Max;
    }
};
