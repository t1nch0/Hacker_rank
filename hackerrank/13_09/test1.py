def fizzBuzz(n):
    # Write your code here
    for i in range(n):
        # print(range(n))
        # n=n+1
        i=i+1
        # print(range(n),i)
        if i<0 or i>200000:
            continue
        if i%3==0 and i%5==0:
            print('FizzBuzz')
        elif i%3==0:
            print('Fizz')
        elif i%5==0:
            print('Buzz')
        else:  
            print (i)
if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)