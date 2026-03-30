def maxProfit(prices: list[int]) -> int:
    buy = 0
    sell = 1
    profit = 0

    while sell < len(prices):
        current = prices[sell] - prices[buy]
        if prices[buy] < prices[sell]:
            profit = max(current, profit)
        else:
            buy = sell
        sell += 1

    
    return profit
        

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
