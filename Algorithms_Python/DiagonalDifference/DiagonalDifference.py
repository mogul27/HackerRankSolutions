import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    
    principal_diagonal = 0
    secondary_diagonal = 0
    
    # Iterate through rows
    for i in range(n):
        # Iterate through column
        for j in range(n):
            
            if i == j:
                principal_diagonal += arr[i][j]
                    
                
            if i + j == n-1:
                secondary_diagonal += arr[i][j]
    
    print(principal_diagonal)
    print(secondary_diagonal)
    
    difference = abs(principal_diagonal - secondary_diagonal)

    return difference
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
