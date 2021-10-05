s = 'PAYPALISHIRING'
numRow = int(input("enter the number of rows: "))
delta = -1
res = [[] for x in range(numRow)]
row = 0

if numRow == 1 or numRow >= len(s):
    print(s)

for i in s:
    res[row].append(i)
    if row == 0 or row == numRow-1:
        delta *= -1
    row +=delta
print(res)
print(len(res))
for i in range(len(res)):
    res[i] = ''.join(res[i])
    print(res)
res = ''.join(res)
print(res)