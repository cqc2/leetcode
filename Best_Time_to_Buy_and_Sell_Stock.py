class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len_ = len(prices)
        if len_ == 0:
            return 0
        
        max_profit = [0]*len_    # max_profit[i] is the max profit attaining if stock sold on day i
        min_price = [0]*len_     # min_price[i] is the min price till day i
        min_price[0] = prices[0]
        i = 1
        while i < len_:
            profit_now = prices[i] - min_price[i-1]
            if profit_now > max_profit[i-1]:
                max_profit[i] = profit_now
            else:
                max_profit[i] = max_profit[i-1]

            if min_price[i - 1] > prices[i]:
                min_price[i] = prices[i]
            else:
                min_price[i] = min_price[i - 1]
            i = i+1
        return max(max_profit)