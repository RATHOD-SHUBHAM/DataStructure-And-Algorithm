# Tc: O(n)
# Sc: O(1)
def getNthFib(n):
    # keep track of the previous 2 fibonacci number
    fib = [0,1]

    i = 3
    while i <= n:
        # calculate the new fibonacci number
        new_fib = fib[0] + fib[1]

        # replace the exisiting number
        fib[0] = fib[1]
        fib[1] = new_fib
        
        i += 1
    
    return fib[1] if n > 1 else fib[0]
