#program to print fibonnanci series!!
n=int(input("enter the term:"))
def fib(n) :

    x=0
    y=1
    if n<=0:
        print("enter a positive integer")
    else:
        print(x)
        print(y)      
    for i in range(2,n):
        z=x+y
        x=y
        y=z
        print(z)
fib(n)

   
