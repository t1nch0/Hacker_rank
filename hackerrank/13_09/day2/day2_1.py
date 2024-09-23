import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    # print(a)
    if len(a)>100:
        quit()
    for num in a:       
        if num>100:
            print('quit because',num)
            quit()
    lst=list()
    count=dict()
    for nim in a:
        count[nim]=count.get(nim,0)+1
    print (count)
    for k,v in count.items():
        tup=(v,k)
        lst.append(tup)
    compi=sorted(lst)
    for k,v in compi[:1]:
        print(v)
        return v
    # print(compi[0])
    
if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'junk.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()