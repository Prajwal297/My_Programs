def selection_sort(list2):
    flag=0
    n=len(list2)
    for i in range(n):
        min=i
        for j in range(i+1,len(list2)):
            if list2[min]>list2[j]:
                min=j
                flag=1
            if flag==1:
                list2[min],list2[i]=list2[i],list2[min]
numlist=[1,3,4,6,8,9,13,61,400,560]
selection_sort(numlist)
for i in range(len(numlist)):
    print(numlist[i],end=" ")
