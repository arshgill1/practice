"""
sort the array
successor=next smallest element
predecessor= next largest element
while left<right:
    find mid(left+right)//2
compare the value smaller or larger
update middle based on comparison if val is smaller or larger
"""

pos = -1

def binary(list,n):

    l = 0
    u = len(list)-1
    while l <= u:
        mid = (l+u) // 2
        if list[mid] == n:
            globals() ['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1
    return False

list = sorted([5, 7, 2, 9, 1, 4, 8])
print("list: ",list)
n = 8

if binary(list, n):
    print(n,"Found! pos:", pos)
else:
    print("Not Found!")
