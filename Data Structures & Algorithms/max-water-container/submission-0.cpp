class Solution {
public:
    int maxArea(vector<int>& heights) {
        int p1, p2;
        int current_space;
        int max_so_far = INT_MIN;
        p1 = 0;
        p2 = heights.size() - 1;
        while(p1 < p2)
        {
            if (heights[p1] < heights[p2])
                current_space = (p2 - p1) * heights[p1];
            else
                current_space = (p2 - p1) * heights[p2];
            if (current_space > max_so_far)
                max_so_far = current_space;
            if (heights[p1] > heights[p2])
                p2--;
            else
                p1++;
        }
        return max_so_far;
    }
};
