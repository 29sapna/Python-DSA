myself = "Sapna,Tiwari"
print(len(myself))
print(myself[0:4])               #slicing is always in square bracket
print(myself[:4])
print(myself[:])                 #it print length of string
print(myself[0:-3])
       #OR
print(myself[0:len(myself)-3])      #12-3=9ans
print(myself[-1:-4])   #length of string -1 and length of string -4=11:8
#STRING ARE IMMUTABLE
a = "Sonalll"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("l"))
print(a.replace("Sonal","Sapna"))
print(a.split(" "))   #split is method which create list
b= "sona is GUD girl"
print(b.capitalize())
print(a.count("Sonal"))
print(a.find("o"))
c= "welcome"
print(c.isalnum())
d ="thanks23"
print(d.isalpha())
e= "   "
print(e.isspace())

#DECISION MAKING
#IF-ELSE statement
#Conditional operators >, <, >=, <=, ==, !=
a = int(input("enter your age"))
print("Your age is: ", a)
if(a>18):
    print(" U become adult")
    print("YES")
else:
    print("U are child")
    print("NO")

#ELIF STATEMENT
num = int(input("Enter the value of num: "))
if(num < 0):
    print("Number is negative.")
elif(num == 0):
    print("Number is Zero.")
else:
    print("Number is positive.")

#NESTED ELIF STATEMENT
num = 18
if (num < 0):
    print("number is negative")
elif (num > 0):
    if(num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <=20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")


#self-problem
import time
t= time.strftime('%H:%M:%S')
hour= int(time.strftime('%H'))
hour = int((input("Enter hour: ")))
print(hour)

if(hour>0 and hour<12):
    print("good morning!!")
elif(hour>12 and hour<17):
    print("good afternoon")
else:
    print("good night")


#SWITCH CASE
x = int(input("Enter the value of x: "))
match x:
    case 0:
        print("x is zero")
    case 1:
        print("case is 1")
    case 2:
        print("case is 2")
    case _:
        print(x)

#LOOP
name = 'Aditya'
for i in name:
    print(i)
    if(i == "d"):
        print(" I LOVE HIM!!")

colors =["Red","Green","Blue","white"]
for i in colors:
    print(colors)
    for i in colors:
        print(i)

for k in range(5):
    print(k + 1)

for k in range(1, 9):
    print(k)

for k in range(1, 12, 3):
    print(k)


#WHILE
for i in range(3):
    print(i)
i=0
while(i<=3):
    print(i)
    i = i + 1
print("Done with the loop")

i=int(input("Enter the numbers: "))
while(i<=38):
    i=int(input("Enter the number: "))
    print(i)
print("Done with the loop")

count = 5
while (count > 0):
    print(count)
    count = count - 1
else:
    print("I am inside else")


#break & Continue
for i in range(12):
    if(i == 10):
        break
    print("5 *", i+1, "=", 5 * (i+1))
    print("loop ko chod k nikal gaya")

#continue
for i in range(12):
    if(i == 10):
        print("skip the iterator")
        continue
    print("5 *", i, "=", 5 * i)

#function
def calculateGmean(a , b):
    mean= (a+b)/(a+b)
    print(mean)

a = 9
b = 8 
def isGreater(a , b):
    if(a>b):
     print("First number is greater")
    else:
     print("Second number is greater")
isGreater(a , b)     
calculateGmean(a , b)  
c = 8
d = 7
calculateGmean(c , d)


#2-function
def average(a , b):
    print("The average is", (a+b)/2)
average( 2,4)

#3function*TUPLE
def average(*numbers):
    sum = 0
    for i in numbers:
     sum = sum + i
    print("Average is: ",sum / len(numbers))
average(9,8,7,1)

#4function**DICTONARY
def name(**name):
    print("Hello,", name["fname"],
name["mname"], name["lname"])
name(mname = "sapna", lname ="silo", fname ="monu")
   
num = int(input("Enter the value of num: "))
if(num < 10,000):
    print(" i am mananger here!")
elif(num > 15,000):
    print("i am devloper here!")
else:
    print("i am employee here!")

a,b=input().split()
print(a,b)

a,b=input()
print(a,b)

a= input().split()   #it is converted into list
print(a)

a,b=input().split()
b=int(b)
print((type(a), type(b)))

#memebership operator
if 'a'in "sapna":
    print("found")
else:
    print("notfound")

i=1
while i<=10:
    print(i, end=" ")
    i+=1
else:
    print("Loop completed", i)

i=11
while (1):
    print(i, end=" ")
    if i>10:
        break
    i+=1
else:
    ("Loop statement")
 
import random
secretno = random.randint(1,100)
guess=int(input("Guess the scret number,"))
guess=secretno+1

while guess!=secretno:
    if(guess<=0):
        print("So sorry! tHat u are quitting!")
        break
    elif(guess>secretno):
        print("you guess is too large.Try again")
        break
    elif(guess<secretno):
        print("you guess is too small.Try again")
        break
else:
    print("Congratulation!you won")
