s = 'PAYPALISHIRING'
numRow = int(input("enter the number of rows: "))

if numRow == 1:
    print(s)

cycle = 2 * numRow - 2
result = []
for i in range(numRow):
    for j in range(i,len(s),cycle):
        result.append(s[j])
        mid_row = j+cycle-(numRow*2)
        if i != 0 and i !=numRow - 1 and mid_row < len(s):
            result.append(s[mid_row])

print("".join(result))