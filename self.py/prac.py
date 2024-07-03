# l=4
# b=2
# h=1
# rect=l*b*h
# print(rect)

# P=2
# R=3
# T=1
# SI=P*R*T/100
# print(SI)

# n=int(input("enter digit: "))
# n=n//10
# print(n)

# a=2
# b=3
# print(a,b)45
# a,b==b,a
# print(b,a)

#print ("divisible by 5" if int(input())%5==0 else "not divisible"
 
# l = "sapna","apple","ball"
# for word in l:
#     for char in word:
#      print(ord(char))


# n = int(input())
# count=1
# if count<=3:
#    print("this is three digit number")
# elif count!=3:
#    print("not three digit number")
# else:
#    print("random number")

# year=int(input("enter the year: "))
# if year%4==0:
#    print("leap year")
# elif year%400==0:
#    print("leap year")
# else:
#    print("not a leap year")

n=real(int(input()))
m=imag(int(input()))
print(real(n))
print(imag(m))
if n>0 and m<0:
   print("real is greater")
elif m>0 and n<0:
   print("imaginary is greater")
else:
   print("both are equals")


N=1
while(N<=10):
   print(N, end=' ')
   N +=1

i=1
while(i<=5):
   print("sapna")
   i+=1

n=6
i=1
s=0
while(i<=n):
   s=s+i
   i+=1
print(s)


n=int(input())
i=2
while i<n-1:
   if n%i==0:
      break
   i+=1
if i==n:
   print("prime")
else:
   print("not prime")


n=10
i=1
sum=0
while(i<=n):
#    print(i)
#    print(i**2)
     sum=sum+i
     print(sum)
     i+=1

n = 100
i = 1
while i <= n:
    if i % 2 != 0:  # Check if the number is odd
        print(i)
    i += 1

n = 100
i = 1
while i <= n:
   if i % 2 == 0:
        print(i)
   i += 1

n=10
i=n 
while i <=1:
   if  i % 2 != 0:
      print(i)
   i -= 1

n=5
fact=1
i=n
while i>=1:
   fact *= i
   print(fact)
   i -= 1

i=1
while(i<=19):
   print(i, end=' ')
   i+=2

def decoration(perform):
  print("*************")
  print("****"+perform()+"****")
  print("*************")
   
@decoration  
def perform():
   return "sapna"
