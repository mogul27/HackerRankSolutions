##### This is a work in progress - need to learn about prefix sums before attempting to get all cases passing -> there is a weird edge case


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

def arrayManipulation(n, queries):
    
    # Create 1-indexed array of 0s
    row = [0 for i in range(n)]
    
    for query in queries:
        start = query[0]
        stop = query[1]
        addition = query[2]
        
        add_row = [0 for i in range(n)]
        add_row[start-1:stop-1] =  [addition] * (stop+1-start)
        row = [sum(x) for x in zip(row, add_row)]
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