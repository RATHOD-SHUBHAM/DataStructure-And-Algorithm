# when ever you dont know how to approach a problem go by sorting the input
# O(nlogn)
def sortFunc(str_inp):
    str_inp = sorted(str_inp)
    for i in range(len(str_inp)-1):
        if str_inp[i] == str_inp[i+1]:
            return False
    return True

# we can use dictionary: Additional data structure
def dataStr(str_inp):
    dict = {}

    for i in range(len(str_inp)):
        if str_inp[i] in dict:
            return False
        dict[str_inp[i]] = i
    return True

# we can perform using bitwise calculation:

if __name__ == '__main__':
    str_inp = input("enter a string: ")
    # myFunc = sortFunc(str_inp)
    myFunc = dataStr(str_inp)
    print(myFunc)



