import os
def findMedian(arr):
    # Write your code here
    # print(sorted(arr), n)
    if n>1000000:
        # print('daaa')
        quit()
    for i in arr:
        if i>10000 or i<-10000:
            # print('more thean 1kk')
            quit()
    if len(arr)%2==0:
        # print('par')
        quit()
    index=int(len(arr)/2)
    median=sorted(arr)[index]
    print(median)   
    # median=
if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'junk.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = findMedian(arr)
    fptr.write(str(result) + '\n')
    fptr.close()