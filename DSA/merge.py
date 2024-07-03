def merge_sort(list1):
    if len(list1)>1:
        mid=len(list1)//2
        leftlist=list1[:mid]
        rightlist=list1[mid:]
        merge_sort(leftlist)
        merge_sort(rightlist) 

        i=j=k=0
        while i<len(leftlist) and j<len(rightlist):
            if leftlist[i]<rightlist[j]:
               list1[k]=leftlist[i]
               i+=1
            else:
                list1[k]=rightlist[j]
                j+=1
            k+=1
        while i<len(leftlist):
            list1[k]=leftlist[i]
            i+=1
            k+=1
        while j<len(rightlist):
            list1[k]=rightlist[j]
            j+=1
            k+=1
mylist=[3,56,12,45,78,9]
merge_sort(mylist)
print(mylist)