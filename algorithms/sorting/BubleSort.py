"""
iterate and swap through the list
after every iteration you get one number(largest) sorted at the end
keep iterating until the whole list is sorted or the condition for i is met

"""

def bubble_sort(n):
    for i in range(len(l) - 1, 0, -1):
        for j in range(i):
            if l[j] > l[j + 1]:
                l[j],l[j+1]=l[j+1],l[j]
                #temp = l[j]
                #l[j] = l[j + 1]
                #l[j + 1] = temp
                
l = [5, 7, 2, 9, 1, 4, 8]
bubble_sort(l)
print(l)
print("len of l: ", len(l))
u=len(l)
print(u)
