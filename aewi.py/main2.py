#OPERATORS
print(3 > 2)
print(3 == 3) #comparison operator

#logical operator
#OR operator
print(3 > 2 and 2 > 6)
#NOT OPERATOR
print(not 3 > 2)
age = 19
if age >= 18:
    print("you are an adult")
    print("you can vote")
elif age < 18 and age > 3:
    print("you are in school")
else:
    print("you are a child")     

    #PROJECT CALCULATOR
first = input("enter first  number: ")
operator = input("enter operator (+,-,*,,/,%)): ") 
second = input("enter second number: ")

first = int(first)
second = int(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second) 
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second) 
elif operator == "%":
    print(first % second) 
else:
    print("invalid operator")            


#RANGE
numbers = range(5)
print(numbers)

#WHILE LOOP
i =1
while i <= 5:
    print(i * "*")
    i = i + 1

#FOR LOOP
for item in range(5):
    print(item + 1)       

#LIST DATATYPE
marks = [97, 98, 67]
marks.append(99) # adding 99 in last of the string
marks.insert(0, 99) # 0 is index, 99 join at starting point
print(marks[-1])        #here -1 stands for backcounting
print(marks[0:2]) #here only 0,1 can apper not 2
print(marks[1:3]) #here , only 1 & 2 can apper 0 &3 can't
print(marks.index("sita"))
for score in marks:
    print(score)

#BREAK & CONTINUE
    #LIST==[]SQUARE BRACKET
students =["ram", "sapna", "sita","moni","soni"]
for student in students:
    if student == "sapna":
        #break; yaha loop khatam ho jata h
        continue; #us string ko chod k sab print kar dets h
    print(student)
#TUPLE---IT IS IMMUTABLE,PARANTHESIS()
    marks =(95, 89, 45, 86, 86)
    print(marks.count(86))
    print(marks.index(86))
    #SET--{} IT CONTAIN ONLY UNIQUE ELEMENT NOT DUPLICATE,UNORDERED
    marks ={34, 67,34}
    print(marks)
    #DICIONARY--CONTAIN  KEY: VALUE
    marks={"english":67, "hindi":78}
    print(marks["english"])
    marks["phy"] = 89
    print(marks)


str1 ="sapna"
str2 ="tiwari"
print("hello", end="\n")
print("hello", end="\n\r")
print("hello", end="\b")
print("hello", end="\r")
print(str1)
print(str2)

print("hello",sep="*", end="+") #only one string separator is not applied
#print(str1,str2,sep="++++++")
print("sapna","tiwari",sep="*****")