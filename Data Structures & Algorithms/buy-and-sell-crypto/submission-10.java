class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int buy = 0; // left
        int sell = 1; // right
        int lastSell, lastBuy;
        
        while(buy != sell && sell < prices.length) {
            int currProfit = prices[sell] - prices[buy];
            if (currProfit > maxProfit)
                maxProfit = currProfit;
            // logic
            if (prices[buy] > prices[sell])
            {
                buy = sell;
                sell++;
            }
            else
                sell++;
        }

        return maxProfit;
    }
}
