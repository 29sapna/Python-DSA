n=int(input())
m=int(input())
for i in range(n):
    for j in range(m):
        if i==0 or i==n-1 or j==0 or j==m-1:
            print('*',end=" ")
        else:
            print("  ",end="")
    print()

print(5 and 6)
print(5 or 6)
print(5 and 6 or 7 and 8)
print(not (5 or 6) or (7 and 8) )

