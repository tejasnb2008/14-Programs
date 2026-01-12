stack = []

def push(stack, item):
    stack.append(item)
    print("Item pushed to stack")

def pop(stack):
    if len(stack) == 0:
        print("Stack is empty (Underflow)")
    else:
        item = stack.pop()
        print("Popped item is:", item)

def display(stack):
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements are:")
        for i in range(len(stack)-1, -1, -1):
            print(stack[i])

while True:
    print("\n1. PUSH\n2. POP\n3. DISPLAY\n4. EXIT")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = int(input("Enter item to push: "))
        push(stack, item)
    elif choice == 2:
        pop(stack)
    elif choice == 3:
        display(stack)
    elif choice == 4:
        break
    else:
        print("Invalid choice")