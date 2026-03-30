<<<<<<< HEAD
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
=======
def maxProfit(prices):
    min_price = prices[0]
    profit = 0
    for p in prices:
        min_price = min(min_price, p)
        profit = max(profit, p - min_price)
    return profit

>>>>>>> f5cb43bcc4450bc6796c7cfcb1d86147eba5184c
