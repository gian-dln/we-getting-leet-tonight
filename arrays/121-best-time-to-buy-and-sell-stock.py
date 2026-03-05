def maxProfit(prices: list[int]) -> int:
    buy = 0
    sell =  1
    profit =  0

    while sell < len(prices):
        currentProfit = prices[sell] - prices[buy]
        if currentProfit > 0:
            profit = max(profit, currentProfit)
        else:
            buy = sell 

        sell +=1

    return profit
        

prices = [1,2]  

print (maxProfit(prices))