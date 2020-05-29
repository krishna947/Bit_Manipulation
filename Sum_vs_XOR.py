#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sumXor function below.
def sumXor(n):
    '''
    i=0
    count=0
    for j in range(n+1):
        s=n+i
        x=n^i
        if s==x:
            count += 1
        i += 1
    return count
    '''
    return int(math.pow(2,bin(n)[2:].count('0'))) if n else 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
