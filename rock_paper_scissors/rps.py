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

if __name__ == "__main__":
    # Test out your implementation from the command line
    # with `python rps.py [n]` with different n values
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')