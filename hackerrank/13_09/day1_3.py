import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    newhr=s.split(':')
    print(newhr)
    hr=int(newhr[0])
    if 'AM' in newhr[2] and newhr[0]=='12':
        hr=int(newhr[0])-12
    elif 'PM' in newhr[2] and hr!=12:
        hr=int(newhr[0])+12
    # print('{:02d}'.format(hr))
    final=str('{:02d}'.format(hr))+':'+newhr[1]+':'+newhr[2][0:2]
    print(final)
    return(final)
if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'junk.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()