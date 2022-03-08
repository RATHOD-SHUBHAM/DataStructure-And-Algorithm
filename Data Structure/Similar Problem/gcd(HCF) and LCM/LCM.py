'''

a x b = LCM(a, b) * GCD (a, b)

LCM(a, b) = (a x b) / GCD(a, b)

'''

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a,b):
    return (a * b) / gcd(a, b)

a = 15
b = 20
LCM = lcm(a,b)
print(LCM)