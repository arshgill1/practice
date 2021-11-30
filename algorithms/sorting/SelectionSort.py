"""
the list has two sides left and right
left is the sorted elements and right is unsorted
how to do?
find the min value(take its position) in the list swap the minposition with first element in the list(first after previous sorted)

"""

def selection_sort(n):
    for i in range(len(l)-1):   # iterate i till second last element
        minpos=i
        #print("minpos: ",minpos)
        #print("i: ",i)
        for j in range(i,len(l)):   #iterate j - from i position till last element because every iteration will give min element on the right. 
            #print("j: ",j)
            if l[j] < l[minpos]:    # find minimun value in whole list by comparison
                minpos=j
        temp=l[i]
        l[i]=l[minpos]
        l[minpos]=temp
        print("l: ",l)
l = [5, 7, 2, 9, 1, 4, 8]
selection_sort(l)

#print(l)
#print("len of l: ", len(l))
#u=len(l)
#print(u)
