#!/usr/bin/python

import argparse

#Interative Solution - O(n^2)
def find_max_profit(prices):
    #Set max diff to -Inf
    max_diff = -float('Inf')
    
    #The outer loop controls the sell price index
    for sell_ind in range(0,len(prices)):

        # The inner loop controls the buy price
        for buy in prices[sell_ind+1:]:

            #If the profit(diff) is greater than previous diff, set value:
            if buy - prices[sell_ind] > max_diff:
                max_diff = buy - prices[sell_ind]
    return max_diff


#Sean's Solution - O(n)
def find_mp_rec(prices):
    #keep track of min price we've seen
    #keep track of max profit we've seen so far
    #interate through our prices list an update these two vars

    min_price = price[0]
    max_profit = prices[1] - min_price

    for i in range(1,len(prices)):
        price = prices[i]
        max_profit = max(price - min_price, max_profit)
        min_price = min(price,min_price)
    return max_profit
  
print(find_max_profit([1050, 270, 1540, 3800, 2]))

if __name__ == '__main__':
    # You can test your implementation by running 
    # `python stock_prices.py [prices]` where prices is comprised of
    # space-separated integer values
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))