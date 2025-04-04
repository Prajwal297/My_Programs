# Create an empty stack
stack = []

def display_stack():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Student Marks in Stack (LIFO):")
        for mark in reversed(stack):
            print(mark)
def pop_mark():
      mark=int(input("enter the marks scored : "))
      stack.append(mark)
while True:
    print("1.store mark")
    print("2. Display Stack")
    print("3. Exit")
    choice= input("Enter your choice: ")
    if choice =='1':
        pop_mark()
    elif choice == '2':
        display_stack()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Try again.")

1