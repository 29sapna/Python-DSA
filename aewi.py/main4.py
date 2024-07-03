n = 10
b = [i*i-1 for i in range(1,n+1)]
print(b)

#
# a = int(input())
# b= int(input())
# c=a+b
# if c%2==0 & c%8==0:
# print("good luck")
print("Hey",6,7,sep="~")
print("Sapna",end="Tiwari")

#LIST
list1 =[8,2.3,[-4,5], ["apple","banana"]]
print(list1)

#tuple
tuple1=(("parrot","sparrow"),("Lion","Tiger"))
print(tuple1)

#dictonary
dict1 = {"name":"Sapna","age":20,"canVote":True}
print(dict1)

#simple calculator
a=10
b=2
print("The value of", a, "+",3, "is: ", a+b)
print("The value of", a, "-",3, "is: ", a-b)
print("The value of", a, "*",3, "is: ", a*b)
print("The value of", a, "/",3, "is: ", a/b)

#TYPECASTING
a ="1"
b="2"
print(int(a) + int(b))  #this is called typecasting(string to integer)

#EXPLICIT TYPECASTING, IMPLICIT TYPECASTING
string = "15"
number =7
string_number = int(string)
sum=number + string_number
print("the sum of both numbers is: ",sum)
      
#implicit typecasting
a =7.0
print(type(a))

b=3.0
print(type(b))

c=a+b
print(c)
print(type(c))

#User input 
a = input("enter your name: ")
print("my name is", a)

x= input("enter first number: ")
y= input("enter second number: ")
print(x + y)
print(int(x) + int(y))

#calculate electric bill

unit= int(input("enter the unit: "))
print("unit",unit)
if unit<100:
     print("no chrge",unit)
elif unit>100:
     print("Rs.5 per unit",unit)
elif unit>200:
     print("Rs.10 per unit",unit)

#whole number
num=2343
while(num>0):
     print(num%10,end="")
     num=int(num/10)

#reverse the digit
num= int(input("Enter the numbers: "))
rem=0
while(num>0):
     rem= rem*10  +(num%10)
     num= int(num/100)
print(rem)     
#
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

systems.reverse()

print('Updated List:', systems)
#STRING
naam = "Sapna"
education = "b.tech"
apple = '''myself sapna , i want job right now'''
for character in apple:
    print(character)