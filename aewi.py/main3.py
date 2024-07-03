#FUCTIONS---"IT PERFORM SPECIFIC TASK FOR EACH LIKE REMOTE BUTTON"
#1.IN-BUILD FUCTION EXAMPLE--INT(), STR(),BOOL()***THEY ALREADY EXIST IN PY**
#2.MODULE FUNCTION--WHEN RELATED FUCTION AND VARIABLE USED IN SAME FILE,EX-MATH MODULE (WE WRITE IMPORT MATH)
#3.USER DEFINED FUNCTION

import math
print(dir(math))
from math import sqrt
print(sqrt(4))

marks= [89,43,32] #TUPLE---IT IS IMMUTABLE,PARANTHESIS
marks.insert(0, 23)
print(55 in marks)
print(len(marks))

#USER DEFINED 
#DEF FUNCTION_NAME(PARAMETER):   "WAY TO WRITE CODE"
def print_sum(first , second):
    print(first + second)
print_sum(1, 3)    
#ODD NUMBER
for i in range(1,10):
    if i % 2!=0:
        print(i, end=",")
        
