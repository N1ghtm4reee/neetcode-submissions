class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int Max = 0;
        int MinPrice = INT_MAX;
        int i = 0;
        while(i < prices.size()) {
            MinPrice = min(MinPrice, prices[i]);
            Max = max(Max, prices[i] - MinPrice);
            i++;
        }
        return Max;
    }
};
