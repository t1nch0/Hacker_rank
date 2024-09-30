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
    # Write your code here
    print((arr))
    row=0
    item=0
    diag=0
    diag2=0
    aux=len(arr)
    for n in arr:
        # print(n)
        item=0
        for num in arr[row]:
            # print('item',num,'longiutd', len(arr)-item)          
            if item==row:
                diag=diag+arr[row][row]
            if (item+row)==(len(arr)-1):
                diag2=diag2+arr[row][item]
            item=item+1  
        row=row+1 
        # for num in arr[row]:          
        #     if item==row+len(arr)-aux:                
        #         diag2=diag2+arr[row][len(arr)-aux-1]
        #         print (diag2,arr[row][len(arr)-aux])
        #         aux=aux-1
             
    result=abs(diag-diag2)
    print(result)
    print(diag,diag2)
if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'junk.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()