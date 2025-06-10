#program for sum to entered number.

def sum(n):
     if n<=0:
          return 0
     else:
        return  n+sum(n-1)
print ("the sum of numbers is",sum)
print()
n=int(input("enter the value :"))
print("the sum is",sum(n))

