pos=-1
def linear(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals() ['pos']=i
            return True
        i=i+1
    return False

list=[5, 7, 2, 9, 1, 4, 8]
n=11
if linear(list,n):
         print("Found!")
else:
    print("Not Found!")
