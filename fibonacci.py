def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b
n=int(input("Enter n"))
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")

