import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

# Start by finding first hourglasses possible per row
# array is 6x6 so how many 3s can we fit along that

def hourglassSum(arr):
    
    all_hg_sums = []
    
    # Point end of hourglass roweise at end
    for i in range(2, 6):
    # Point at end of columnwise row starting at 2 - final position it can be is 6 (Per row)
        for j in range(2, 6):
            top_row = sum([arr[i-2][j-2], arr[i-2][j-1], arr[i-2][j]])
            middle_row = arr[i-1][j-1]
            bottom_row = sum([arr[i][j-2], arr[i][j-1], arr[i][j]])
            
            hg_sum = sum([top_row, middle_row, bottom_row])
            all_hg_sums.append(hg_sum)
    
    hg_largest = max(all_hg_sums)
    
    return hg_largest
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()