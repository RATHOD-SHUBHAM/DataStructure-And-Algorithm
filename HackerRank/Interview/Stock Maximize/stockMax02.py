from collections import Counter

def stockmax(prices):
    # Write your code here
    print("prices: ",prices)
    print("\n")
    
    m = prices.pop()
    print("pop: ",m)
    print("\n")
    
    maxarr = Counter()
    print(maxarr)
    
    for i in range(len(prices)-1,-1,-1):
        print("i is: ",i)
        print("\n")
        
        m = max(m , prices[i])
        
        print("m is: ",m)
        
        maxarr[i] = m 
        
    return sum(maxarr[i] - v for i,v in enumerate(prices))


for _ in range(int(input)):
    n = int(input)
    prices = list(map(int,input().split()))
    print(stockmax(prices))
