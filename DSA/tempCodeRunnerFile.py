def selection_sort(list1):
    n=len(list1)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n-1):
            if list1[j]<list1[min_index]:
                min_index=j
        list1[i],list1[min_index]=list1[min_index],list1[i]
l1=[56,90,23,45,89,10]
selection_sort(l1)
print(l1)