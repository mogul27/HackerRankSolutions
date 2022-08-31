import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    
    arr = [[] for j in range(n)]
    lastAnswer = 0
    answers = []
    
    # n is size of array - q is the number of queries
    
    # Query 1
    # Array[0] 
    # Number to do that with
    for query in queries:
        query_type = query[0]
        
        idx = (query[1] ^ lastAnswer) % n
        
        if query_type == 1:
            arr[idx].append(query[2])
            print(arr[0])
            print(arr[1])
            
        elif query_type == 2:
            lastAnswer = arr[idx][query[2] % len(arr[idx])]
            answers.append(lastAnswer)
    
    return answers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()