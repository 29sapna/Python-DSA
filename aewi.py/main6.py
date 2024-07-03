#LIST
marks = [3 ,5, 6, "sona", True, 3 ,5 , 1,7,0]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
#NEGATIVE INDEXING
print(marks[-3]) #marks[len(marks)-3]=5-3=>2indexing is ans here
#SLICING
print(marks[1:4])
print(marks[1:-1])
print(marks[1:3:4])
print(marks[1:9:3]) #jump indexing

list= [i for i in range(4)]
print(list)
list=[i for i in range(10) if(i%2==0)]
print(list)

#method in py
l = [11, 34, 56, 36, 89]
print(l)
l.append(80)
print(l)
l.sort(reverse=True)  #sort in decending order
print(l)
l.reverse()
print(l)
print(l.index(56))
print(l)
print(l.count(11))
print(l)
l.insert(1, 45)
print(l)
m = [12.44,56,33]
k=l+m
print(k)
l.extend(m)
print(l)

#TUPLES: CAN'T BE CHANGED & STRINS TOO ,BUT LISTS CAN BE CHANGED
tup =(1,3,5)
#tup =(1,)  #for one element comma is compulsory
print(type(tup), tup)
print(len(tup))
print(tup[2])
print(tup[-3])
print(tup[:3])
print(tup[1:2])

tupl =(1,1,1,1,1)
t = tupl.count(1)
print(t)

#string formating
letter = "myself {1} and mysister {0}"
sistername = "nandani"
myname ="sona"
print(letter.format(sistername, myname))
print(f"myself {myname} and mysister {sistername}")

price = 52.36987
txt = f"for only {price: .2f} dollars!"
print(txt)

#Docstring
def square(n):
    '''Takes in a number n, return the squares of n'''
    print(n**2)
square(3)
print(square.__doc__)

#factorial(n) = n * factorial(n-1)
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(6))

#set-it does not repeat values,do not changable
s={2,4,2,5,6}
print(s)

sonal={} #empty bracket takes dict here not set
print(type(sonal))

sonal= set()
print(type(sonal))

info={"sona",12,"adi",12,90}
for value in info:
    print(value)


#SET METHOD
s1={2,4,5,3}
s2={4,5}
print(s1.union(s2))
print(s1.intersection(s2))

s1.update(s2)
print(s1, s2)
s1.intersection_update(s2)
print(s1,s2)

print(s1.issuperset(s2))
print(s1.issubset(s2))
s1={2,4,5,3}
s1.remove(4)
print(s1)
del s1
print(s1)

#DICTINORY
dic ={
    34:"baby",
    21:"little",
    37:"old"
}
print(dic[34])

info ={'me':'sapna','age':12}
print(info)
print(info.keys())

#methods used in dictonary
ep1={122:23, 123:54, 567:66}
ep2={245:56, 456:34}

#ep1.update(ep2)
#ep1.clear()
#del ep1()
ep1.popitem()
print(ep1)

#For loop with else
for i in range(6):
    print(i)
    if i == 4:
      break
else:
    print("Sorry no i")     #else is executed when loop is ended


i=0
while i<7:
  print(i)
  i= i+1
  if i == 8:
    break
else:
    print("sorryyy")

