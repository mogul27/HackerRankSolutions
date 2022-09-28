##### This is a work in progress - need to learn about prefix sums before attempting to get all cases passing -> there is a weird edge case
## Prefix summing, steps and falls -> will complete easier ones and come back for this


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n:int, queries:list):
    
    # Create 1-indexed array of 0s
    row = [0 for i in range(n)]
    
    for query in queries:
        to_change = range(query[0]-1, query[1])
        
        for index in to_change:
            row[index] = row[index] + query[2]
    
    print(row)
    return max(row)
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()