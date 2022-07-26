num = int(input('Enter a number to find its factorial : '))
def fact(f):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f
print('Factorial of',num,'is : ',fact(num))
