def selection_sort(n):
    for i in range(len(l)):
        minpos=i
        #print("minpos: ",minpos)
        #print("i: ",i)
        for j in range(i,len(l)):
            #print("j: ",j)
            if l[j] < l[minpos]:
                minpos=j
        temp=l[i]
        l[i]=l[minpos]
        l[minpos]=temp
        print("l: ",l)
l = [5, 7, 2, 9, 1, 4, 8]
selection_sort(l)
print(l)
print("len of l: ", len(l))
u=len(l)
print(u)
