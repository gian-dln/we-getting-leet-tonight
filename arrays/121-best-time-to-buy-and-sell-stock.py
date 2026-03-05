def maxProfit(prices):
    min_price = prices[0]
    profit = 0
    for p in prices:
        min_price = min(min_price, p)
        profit = max(profit, p - min_price)
    return profit

