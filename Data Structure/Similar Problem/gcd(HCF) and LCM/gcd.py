def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = 15
b = 20
GCD = gcd(a,b)
print(GCD)



'''
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

a = 15
b = 20
GCD = gcd(a,b)
print(GCD)



'''