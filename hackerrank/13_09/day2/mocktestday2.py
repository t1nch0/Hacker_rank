
#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#
import os

def flippingMatrix(matrix):
    # Write your code here
    max_num=0
    pos=0
    
    row_cnt=0
    num_cnt=0
    for row in matrix:
        # print('row',row_cnt,'num',num_cnt)
        print (row)
        num_cnt=0
        for num in row:
            print(num)
            if num>max_num:
                max_num=num
                max_pos=[row_cnt,num_cnt]
            num_cnt=num_cnt+1
        row_cnt=row_cnt+1    
    print('numero max y posicion',max_num, max_pos)
    # invertrow(max_pos[0], matrix)
    # invertcol(max_pos, matrix)
    
    return suma()
def invertrow(changer, matrix):
    test=matrix[changer]
    invetida=test[::-1]
    matrix[changer]=invetida
    # print(invetida)
    # print('ror change',matrix)
def invertcol(changec, matrix):
    col_inv=[fila[changec[1]]for fila in matrix][::-1]
    for i, fila in enumerate(matrix):
        fila[changec[1]]=col_inv[i]
    # print('col chjange',matrix)
    # for row in matrix:
def suma():
    sum=0
    for num in matrix[:n]:
        for num2 in num[:n]:
            sum=sum+num2
    print (sum)
if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'junk.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())
    print ('queres son',q)
    for q_itr in range(q):
        n = int(input().strip())
        # print('esta es n', n)
        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))
            # print(matrix)
        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()