def stockmax(prices):
    # Write your code here
    print("prices: ",prices)
    print("\n")
    
    m = prices.pop()
    print("pop: ",m)
    print("\n")
    
    maxSum = 0
    arrSum = 0
    
    for i in reversed(prices):
        print("i is : ",i)
        print("m before max: ",m)
        m = max(m,i)
        print("m after max: ",m)
        print("\n")
        
        maxSum += m
        
        print("max Sum : ",maxSum)
        
        arrSum+= i
        print("arrSum: ",arrSum)
        print("\n")
        
    print(maxSum-arrSum)


for _ in range(int(input)):
    n = int(input)
    prices = list(map(int,input().split()))
    print(stockmax(prices))
