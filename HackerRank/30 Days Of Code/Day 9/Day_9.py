def factorial(n):
    if n == 0:
        print("n is: ", n)
        return 1
    else:
        res = n * factorial(n - 1)
        print("res is: ", res)
        return (res)


print(factorial(3))
