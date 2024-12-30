n = int(input("enter a number of rows : "))
for row in range(1, n + 1):
  
    for space in range(1, (n-row)+ 1):
        print(" ", end="")
    for symbol in range(1, row+1):
        print("\U0001F600",end="")
    
    print()  

