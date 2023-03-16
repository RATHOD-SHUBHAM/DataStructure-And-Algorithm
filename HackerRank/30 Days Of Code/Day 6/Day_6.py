# Enter your code here. Read input from STDIN. Print output to STDOUT
numberofinput = int(input())  # 2
for i in range(numberofinput):
    st = input()
    # hacker
    # Hce akr
    op1 = ""
    op2 = ""
    for i in range(len(st)):
        if i % 2 == 0:
            op1 = op1 + st[i]
        else:
            op2 = op2 + st[i]

    print(op1 + " " + op2)

