def isprime(n):     #for list of numbers
    for i in arr:
        if i > 1:
            for j in range(2, i):
                if i%j==0:
                    print(i, " not prime")
                    break
            else:
                print(i)

def primenum(n):    #for single number
    for i in range(2,x):
        if x>1:
            if x%i==0:
                print("not prime")
                break   #if ones its div & is not prime then why check for other numbers
    else:
        print("prime")

arr=[23,43,46,16,27,38]
isprime(arr)

x=47
primenum(x)

# program to print prime numbers between 100 and 200

n=int(input("enter a number between 100 and 200: "))
while n>99 and n<201:
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break
    else:
        print(n," prime")
    break
