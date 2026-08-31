class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        int profit = 0;
        int left = 0;
        int right = 1;
        while(right < prices.size())
        {
            profit = prices[right] - prices[left];
            maxProfit = std::max(maxProfit, profit);
            if (prices[left] >= prices[right])
                left = right;
            right++;
        }
        return maxProfit;
    }
};
