import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    max,min,aux=0,0,0
    arr.sort()
    for num in range(len(arr)):
        # print(num)
        if num>0:
            max=max+arr[num]
            # print(num) 
        if num<4:
            # print(num)
            min=min+arr[num]          
    print(min, max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
