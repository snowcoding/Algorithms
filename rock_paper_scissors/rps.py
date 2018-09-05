#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    base = [['rock'],['paper'],['scissors']]
    if n==0:
        return [[]]
    if n==1:
        return base

    perms = []    
    for p in rock_paper_scissors(n-1):
        for b in base:
            perms.append(p+b)
    return perms

#Sean's solution:
def rps(n):
    # return an array
    outcomes = []

    #We don't have a list of possible plays
    plays =['r','p', 's']

    #generate a n-length permuatation of possible plays
    #base case when n ==0
    #every time we decrement n, we'll add another play to the list we're generating

    # define a inner recursive helper function
    def generate_plays(rounds_left, result=[]):
        if rounds_left == 0:
            outcomes.append(result)
            return
        for play in plays:
            generate_plays(rounds_left - 1, result + [play])

    generate_plays(n,[])
    
    return outcomes

if __name__ == "__main__":
    # Test out your implementation from the command line
    # with `python rps.py [n]` with different n values
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')