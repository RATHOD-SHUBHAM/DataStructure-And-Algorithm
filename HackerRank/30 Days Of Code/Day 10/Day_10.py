#  the time complexity of bin() for a number n is O(log(n))
#  It is log(n). Think about the simple division, we divide the number by 2 until the remainder becomes 0 or 1 just like tree traversal.


decimal_number = int(input("Enter a decimal Number: "))
# 951
# covert the decimal number into binary

binary_number = bin(decimal_number)
print("Binary conversion of the number is: ",binary_number)

count, maximum = 0, 0
# go through each element and keep a count of max consecutive 1's
for element in binary_number:
    if element == '1':
        count += 1
    else:
        maximum = max(maximum,count)
        count = 0

print(max(maximum,count))
