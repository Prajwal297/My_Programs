def fact(n):
    if n<0:
        print ("Negative numbers are not valid , Please enter a valid number!!")
    elif n==0 or n==1 :
        return 1
    else:
        return n*fact(n-1)
print()
n=int(input("enter the value :"))
Ans=fact(n)
print("The factorial value is ",Ans)
    