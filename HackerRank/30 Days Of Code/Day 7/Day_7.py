# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
name_number = [input().split() for _ in range(n)]
phone_book = {key:val for key,val in name_number}

while True:
    try:
        name = input()
        if name in phone_book:
            print("%s=%s" %(name,phone_book[name]))
        else:
            print("Not found")
    except:
        break
