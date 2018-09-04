#!/usr/bin/python

import argparse

#Interative Solution
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

  
print(find_max_profit([1050, 270, 1540, 3800, 2]))

if __name__ == '__main__':
    # You can test your implementation by running 
    # `python stock_prices.py [prices]` where prices is comprised of
    # space-separated integer values
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))