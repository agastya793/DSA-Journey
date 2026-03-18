
'''Problem : best time to buy and sell stock
   time complexity: O(n)
   space complexity: O(1)'''

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # Step 1: Update minimum price
        if price < min_price:
            min_price = price

        # Step 2: Calculate profit
        profit = price - min_price

        # Step 3: Update max profit
        if profit > max_profit:
            max_profit = profit

    return max_profit


prices = [7,1,5,3,6,4]
print(maxProfit(prices))  