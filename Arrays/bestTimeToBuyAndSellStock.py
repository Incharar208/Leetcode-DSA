class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      #keeping buy and sell and updating values of buy and sell and finding corresponding maximum 
        buy = 0
        sell = 1
        maxProfit = 0
        while sell < len(prices) :
            if prices[sell] < prices[buy] :
                buy = sell
            else :
                maxProfit=max(maxProfit,(prices[sell]-prices[buy]))

            sell = sell + 1

        return maxProfit        
