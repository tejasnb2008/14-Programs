def fibonacci(n):
    if n <= 0:
        print("Please enter a positive integer")
        return None
    a, b = 0, 1
    print("Fibonacci series is:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

num = int(input("Enter a number to generate the Fibonacci series: "))
fibonacci(num)