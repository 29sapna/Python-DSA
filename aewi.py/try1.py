# # n= int(input("enter a number: "))
# # if n==0 or n==1:
# #     print("its an invalid number!")
# # elif n%2==0:
# #     print("it's not a prime number")
# # else:
# #     print(n," is a prime number:")


# from collections import Counter


# n=500
# l=[]
# for i in range(1,32):
#     m=(10>>i &1)
#     l.append(m)

# print(str(l))


# num=15
# c=1
# sum=0
# while c<=num:
#     sum=sum+c**2   
#     c+=1
#     print(sum)

# name='parul'
# college='parul'
# print(id(name))
# print(id(college))
   

# name='parul'
# college=''
# for i in name:
#     college=college+i
# print(id(name))
# print(id(college))

# name='parul'
# name1=name[:5] +' '
# print(id(name))
# print(id(name1))

# print('308'>'32')


# #conversion by capital to small
# name='PaRUl'
# new=' '

# for i in name:
#     if(ord(i)>64 and ord(i)<91):         #unicode for capital letter :65 to 90 , and small letter :97 to 122
#         new+= chr(ord(i)+32)
#         print(new)
#     elif(ord(i)>86 and ord(i)<127):
#         new+= chr(ord(i)-32)
#         print(new)
#     else:
#         new+=i
#         print(new)


# # pyramid alphabet pattern
# n = 3
# for i in range(n):
#     for j in range(n - i - 1):
#         print(' ', end='')
#     for k in range(2 * i + 1 ):
#         print(chr(65 + k), end='')
#     print()
   
# str="Parul"
# str1="Parul university" 
# n1=len(str)
# n2=len(str1)
# for i in range(n1):
#     if(str1==str)[i:i+n2]:
#      Counter+=1
     

    
# tuple=(3,5,5,5['a','abc','4.5'],'hi')
# res=tuple.count(5)
# print(res)
# tuple[2][1]='parul'
# print(tuple)
# tuple[2]=tuple(tuple[2])
# print(tuple)


# sum=int(input())
# list=[2,4,5,3,6]

# for i in range(len(list)):
#     for j in range(i+1(len(list))):
#      if :
#          target=list[i]+list[j]
#          target==sum
#          print(list[i],list[j])
    

set1={1,2,3,4}
set2={4,5,6,7}
set=set1.union(set2)
print(set)

set1={1,2,5,4}
set2={4,5,6,7}
set=set1.intersection(set2)
print(set)

set1={1,2,3,4}
set2={4,2,6,7}
set=set1-(set2)
print(set)

set1={1,2,3,4}
set2={4,2,6,7}
set=set1^(set2)
print(set)

n=5
set1=set()
set2=set()
for i in range(1,n+1):
    set1.add((n-1)*i)
    set2.add((n+1)*i)
print(set1,set2)
print(set2.symmetric_difference(set1))

total_runs={'p1':431, 'p2':247, 'p3':378}
present_runs={'p1':76, 'p2':0 ,'p3':104}
for i in present_runs.keys():
  for j in total_runs.keys():
    total_runs[j]+= present_runs[i]
    print(total_runs)

def table(m,n):
   if(n==1):
      print("{}  *  {} = {}".format(m, n, m*n))
      return
   
   table(m, n-1)
   print("{}  * {} = {}".format(m, n, m*n))

m,n=tuple(map(int, input().split()))
table(m,n)




