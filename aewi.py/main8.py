import math    #1 method of using import
result = math.sqrt(9)
print(result)

from math import sqrt,pi   #2 method  to use import
result =sqrt(9) * pi
print(result)

import math as m
result = m.sqrt(9) *m.pi
print(result)

def welcome():
    print("Welcome to u.s.a")

print(__name__)    
if __name__ == "__main__":
    welcome()

import os    #os modules

# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0, 10):
#     os.mkdir(f"data/Day{i+1}")

for i in range(0, 10):
    os.rename(f"data/Day{i+1}", f"data/Tutorial{i+1}")


#LOCAL & GLOBAL VARIABLE
x = 10 #global variable

def my_function():
    global x
    x = 4
    y =5 #local variable
    print(y)

my_function()
print(x)
#print(y)   #this will cause an error because y is a local variable and is not accessible outside of the function

#file IO
f = open('file.txt', 'r')
text = f.read()
print(text)
f.close()

#WRITING A FILE
f = open('file.txt','a')
f.write('baby, we are small')
f.close()

with open('file.txt', 'a'):
    f.write("hey i am inside with")


#READLINES() METHOD
f= open('file.txt', 'r')
i=0
while True:
    i = i+1
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print("Marks of students {i} in math is: {m1}")
    print("Marks of students {i} in sst :{m2}")
    print("Marks of students {i} in sci is:{m3}")
    
    print(line)

#seek  & tell function
with open('file.txt','r') as f:
    print(type(f))
    f.seek(5)
    print(f.tell)
    f.write('sapna')
    f.truncate(5)

    data = f.read(2)
    print(data)

#LAMBDA FUNCTION
double = lambda x: x * 2
cube = lambda x: x*x*x
avg = lambda x, y ,z:(x+y+z)/2

print(double(5))
print(cube(5))
print(avg(3,5,8))

#MAP,FILTER,REDUCE
def cube(x):
    return x*x*x

print(cube(2))
l =[1, 3, 5, 7]
newl =list(map(cube, l))
print(newl)

#FILTER
def filter_function(a):
    return a>2
newnewl = list(filter(filter_function, l))
print(newnewl)

name=input("enter the name:")
vowels=list(filter(lambda ch: ch in  "aeiou",name))
if len(vowels)==0:
    print("no vowels in your name")
else:
    print("Vowels in ypur name:", vowels)

#reduce
from functools import reduce
numbers = [1, 2, 3, 4, 5]
def mysum(x,y):
    return x + y
sum = reduce(mysum, numbers)
print(sum)

# "is" & "=" operator
#is-locate exact location of object in memory,verify identity
#"=" value

a = 2
b = 2

print(a is b)
print(a == b)

n=list(int(input()))
print("The list is: ")