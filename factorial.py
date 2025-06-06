def fact(n):
    if n==0 or n==1 :
        return 1
    else:
        return n*fact(n-1)
print()
n=int(input("enter the value :"))
An=fact(n)
print("The factorial value is ",An)
    