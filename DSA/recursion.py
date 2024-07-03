def printN(n):
    if n>0:
        printN(n-1)
        print(n , end=" ")
printN(10)

def printNreverse(n):
    if n>0:
        print(n, end=" ")
        printNreverse(n-1)
        
printNreverse(10)

def printoddN(n):
    if n>0:
        printoddN(n-1)
        print(2*n-1,end=' ')
printoddN(10)

def printevenN(n):
    if n>0:
        printevenN(n-1)
        print(2*n,end=' ')
printevenN(10)

def printevenN(n):
    if n>0:
        print(2*n,end=' ')
        printevenN(n-1) 
printevenN(10)

def sumN(n):
    if n==1:
        return 1
    return n+sumN(n-1)
def sumNodd(n):
    if n==1:
        return 1
    return 2*n-1 +sumNodd(n-1)
def sumN(n):
    if n==1:
        return 1
    return n+sumN(n-1)
def sumNodd(n):
    if n==1:
        return 1
    return 2*n-1 +sumNodd(n-1)
def sumNEven(n):
    if n==1:
        return 2
    return 2*n + sumNEven(n-1)
print(sumNEven(10))
def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)
print(fact(4))
def sqsum(n):
    if n==1:
        return 1
    return n*n + sqsum(n-1)
print(sqsum(3))


