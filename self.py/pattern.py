# def Swap(a,b):
#     a=a+b
#     b=a-b
#     a=a-b
#     print(a,b)
# a=int(input())
# b=int(input())
# print(a,b)
# Swap(a,b)
def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*",end=' ')
        print() 


def pattern2(n):
    for i in range(n):
        for j in range(n-i):
            print("#", end="-")
        print()

def pattern3(n):
    for i in range(n):
        for j in range(1,n-i+1):
            print(j, end='')
        print()

def pattern4(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end='')
        print()
def pattern5(n):
    for i in range(1, n-j+1):
        for j in range(n):
            print(j,end='')
        print()
def pattern6(n):
    for i in range(n):
        for j in range(n-i-1):
            print('-',end='')
        for j in range(i+1):
            print("*",end='')   
            
        print()  
def pattern7(n):
    m=1
    for i in range(n):
        print(i,'.',end=' ')
        for j in range(i+1):
            print(m,end=' ')
        print()
        m += 1
def pattern8(n):
    for i in range(n):
        for j in range(1,n-i+1):
            print(j,end='')
        print()        
def pattern9(n):
    for i in range(n):
        for j in range(n , i,-1):
            print(j , end='')
        print()
def pattern10(n):
    num=1
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end=' ')
        for k in range(num):
            print("*",end=' ')
            
        for l in range(n-i-1):
            print(" ",end=' ')

        print()
        num += 2
n=5
pattern10(n)
