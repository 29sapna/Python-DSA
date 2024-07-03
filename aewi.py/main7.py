#EXCEPTION HANDLING
a= input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
   for i in range(1,11):
    print(f"{int(a)} *  {i} = {int(a)*i}")
except Exception as e:
  print(e)
print("some one like you")
print("someone loves you")

try:
  num= int(input("Enter an integer: "))
  a= [9,7]
  print(a[num])
except ValueError:
  print("Number entered is not an integer")
except IndexError:
  print("Index Error")

def func1():
  try:
    l=[1,2,3,4]
    i=int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("errorrrrr")
    return 0
   #finally:
    print("it is defined as it is always executed")

x=func1()
print(x)

#raise error
a = int(input("Enter any value between 5 and 9"))
if(a<5 or a>9):
  raise ValueError("value should be between 5 and 9")

#if else in one line
a= 30
b= 40
print("A") if a > b else print("=") if a == b else print("B")

c=9 if a>b else 0
print(c)

#Enumerate function
marks = [12, 34, 56, 64, 98, 36]
index = 0
for mark in marks:
  print(mark)
  if(index == 3):
    print("Sonal")
  index +=1


for index, mark in enumerate(marks , start=1):
  print(mark)
  if(index == 3):
    print("Sonal here!")