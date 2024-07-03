
# def fibonacci(n):
#     a = 0
#     b = 1 
#     c = 0 
#     print(a,b,end=" ")
#     for i in range(2,n):
#         c=a+b
#         print(c,end=" ")
#         a,b=b,c
# def prime(n):
#     if n==0 or n==1:
#         return 'invalid'
#     elif n%2==0:
#         return 'not prime'
#     else:
#         return 'prime'
def palindrom(n):
    num = n
    rev = 0
    while n != 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10

    if rev == num:
        print("palindrome")
    else:
        print("not palindrome")

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def Armstrong(n):
    num=n
    sum=0
    while(n!=0):
        rem=n%10
        sum=sum+rem**3
        n=n//10
    
    if sum==num:
        print("Armstrong")
    else:
        print("Not armstrong")

def SumDigit(n):

    sum=0
    while(n!=0):
        m=n%10
        sum=sum+m
        n=n//10

    print(sum)

def Reverse(n):
    
    rev=0
    while(n!=0):
        rem= n%10
        rev= rev*10 + rem
        n=n//10
    print(rev)
n = int(input("Enter a number: "))

def Swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    print(a,b)
a=int(input())
b=int(input())
print(a,b)
Swap(a,b)





