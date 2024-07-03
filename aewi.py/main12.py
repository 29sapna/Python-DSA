n= int(input())
#print("even") if n/2==2*n//2 else print("odd")
r=n-(n//10)*10
if r==0 or r==2 or r==4 or r==6 or r==8:
    print("even")
else:
    print("odd")



