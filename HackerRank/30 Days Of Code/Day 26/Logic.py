# Enter your code here. Read input from STDIN. Print output to STDOUT
def Convert(string):
    li = list(string.split(" "))
    return li


date_returned = input()
date_returned = Convert(date_returned)
date_returned = list(map(int, date_returned))
# print(date_returned)
date_due = input()
date_due = Convert(date_due)
date_due = list(map(int, date_due))
# print(date_due)


# if returned within same month but different date
if date_returned[0] > date_due[0] and date_returned[1] == date_due[1] and date_returned[2] == date_due[2]:
    print(15*(date_returned[0]-date_due[0]))
# if returned with different month
elif date_returned[1] > date_due[1] and date_returned[2] == date_due[2]:
    print(500*(date_returned[1]-date_due[1]))
elif date_returned[2] > date_due[2]:
    print(10000)
else:
    print(0)

