def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

def sum_of_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum

while True:
    print("Menu:")
    print("1. Find Factorial")
    print("2. Find Sum of Numbers")
    print("3. Exit")
    choice = int(input("Enter your choice(1/2/3): "))
    if choice == 1:
        num = int(input("Enter a number: "))
        print("Factorial", factorial(num))
    elif choice == 2:
        num = int(input("Enter a number: "))
        print("sum of numbers", sum_of_numbers(num))
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again!")