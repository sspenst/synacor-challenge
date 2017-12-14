"""
Script for figuring out coin order for the Ruins puzzle.
"""

import itertools
import sys

coins = {
    '2':'red',
    '3':'corroded',
    '5':'shiny',
    '7':'concave',
    '9':'blue'
}

for perm in itertools.permutations('23579', 5):
    n = [int(c) for c in perm]

    res = n[0] + (n[1]*n[2]*n[2]) + (n[3]*n[3]*n[3]) - n[4]
    
    if res == 399:
        for c in perm:
            print(coins[c] + ' coin')
        sys.exit()