class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy = curr = maxp = 0
        # profit = 0
       
        # while curr < len(prices):
        #     if prices[curr] < prices[buy]:
        #         buy = curr
        #     if prices[curr] > prices[buy]:
        #         maxp = max(maxp,prices[curr])
        #         #sell = prices.index(maxp)
        #         profit = maxp - prices[buy] 

        #     curr += 1
        # return profit
        mini = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            cost = prices[i] - mini
            max_profit = max(max_profit,cost)
            mini = min(mini,prices[i])

        return max_profit

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna