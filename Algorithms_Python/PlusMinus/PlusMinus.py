import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    
    total_count = len(arr)
    pos_count = len([element for element in arr if element > 0])
    neg_count = len([element for element in arr if element < 0])
    zero_count = len([element for element in arr if element == 0])
    
    proportion_arr = [float(pos_count)/float(total_count), float(neg_count)/float(total_count), float(zero_count)/float(total_count)]
    
    for prop_arr in proportion_arr:
        print("{:.6f}".format(prop_arr))
        
    
    

if __name__ == '__main__':
    n = int(raw_input().strip())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)
    
        