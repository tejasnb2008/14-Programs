queue = []

def enqueue(queue, item):
    queue.append(item)
    print("Item added to queue")

def dequeue(queue):
    if len(queue) == 0:
        print("Queue is empty (Underflow)")
    else:
        item = queue.pop(0)
        print("Removed item is:", item)

def display(queue):
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue elements are:")
        for i in queue:
            print(i, end=" ")
        print()

while True:
    print("\n1. ENQUEUE\n2. DEQUEUE\n3. DISPLAY\n4. EXIT")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = int(input("Enter item to add: "))
        enqueue(queue, item)
    elif choice == 2:
        dequeue(queue)
    elif choice == 3:
        display(queue)
    elif choice == 4:
        break
    else:
        print("Invalid choice")



MYSQL