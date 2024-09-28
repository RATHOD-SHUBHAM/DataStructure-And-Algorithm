# Using 2's Compliment

def get_rightmost_set_bit(n):
    return n & -n

print(get_rightmost_set_bit(12))


# Using Bit Manipulation

def get_rightmost_set_bit(n):
    return n & ~(n - 1)

print(get_rightmost_set_bit(12))