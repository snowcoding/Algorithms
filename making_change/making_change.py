#!/usr/bin/python

import sys

# def making_change(amount, denominations):
#   cache = [i in i for range(0,n)]
#   if amount <= 0:
#     return 0
#   elif amount == 1 or amount == 2 or amount == 3 or amount == 4 
#     cache[amount] = 1
#     return cache[amount]
  

#Sean's recursive solution
def making_change(amount, denominations):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    #what if the amount is +, but we have no denominations?
    if len(denominations) <= 0 and amount > 0:
        return 0

    #The first recursive call get us to the 1st two base cases while the 2nd recursive call get us to the 3rd base case:
    return making_change(amount-denominations[-1],denominations) + making_change(amount, denominations[:-1])

#Cached solution with interative ~ O(n*m)
def making_change(amount, denominations):
    # init the cache
    cache = [0 for _ in range(amount + 1)]
    cache[0] = 1

    # loop through denom
    for coin in denominations:
        for higher_amount in range(coin, amount+1):
            remainder = higher_amount - coin
            cache[higher_amount] += cache[remainder]
    
    return cache[amount]


if __name__ == "__main__":
  # Test out your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")