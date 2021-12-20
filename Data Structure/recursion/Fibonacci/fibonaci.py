def fib(n):
    # base condition
    if n <= 1:
        return n
    Fibonacci_sequence = fib(n-1) + fib(n-2)

    return Fibonacci_sequence


if __name__ == '__main__':
    n = int(input("Enter the nth term you want to find out: "))
    if n < 0:
        print("print invalid input")
    else:
        print(fib(n-1))