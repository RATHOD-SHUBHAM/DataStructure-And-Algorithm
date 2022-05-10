n = int(input("Enter the number of entries you want in the phone book: "))
#todo:  take input from user and convert it into a list
name_number = [input("Enter the name and number: ").split() for _ in range(n)]
# print(name_number)
#todo:  convert the list into a dictionary
phone_book = {key: value for key, value in name_number}
# print(phone_book)

while True:
    try:
        name = input("Enter the name you want to check in phone book: ")
        if name in phone_book:
            print("%s = %s" %(name,phone_book[name]))
            break
        else:
            print("not Found")
            break
    except:
        break
