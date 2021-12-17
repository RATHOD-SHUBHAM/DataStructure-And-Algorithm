def recursion(n):
    if n < 0:
        return
    print(n)
    recursion(n-1)


if __name__ == '__main__':
    recursion(5)