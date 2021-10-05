def longestPalSubstr(st):
    n = len(st)  # get length of input string
    print("the value of n is : ",n)
    print("\n\n\n")

    # table[i][j] will be false if substring
    # str[i..j] is not palindrome. Else
    # table[i][j] will be true
    table = [[0 for x in range(n)] for y
             in range(n)]

    # All substrings of length 1 are
    # palindromes
    maxLength = 1
    i = 0
    start = 0
    while i < n:
        print("am here")
        table[i][i] = True
        i = i + 1

    # check for sub-string of length 2.

    i = 0
    while i < n-1:
        print("here")
        if st[i] == st[i + 1]:
            table[i][i + 1] = True
            start = i
            maxLength = 2
        i = i + 1

    # Check for lengths greater than 2. so it starts with 3
    # somethng like for k=3; k<=n; k++
    # k is length of substring
    k = 3
    while k <= n:
        print("hello")
        # Fix the starting index
        i = 0
        while i < (n - k + 1):
            print("the n value is : ",n)
            print("the k value is : ",k)
            print("the i value is : ",i)

            # Get the ending index of
            # substring from starting
            # index i and length k
            j = i + k - 1
            print("j value is : ",j)

            # checking for sub-string from
            # ith index to jth index iff
            # st[i + 1] to st[(j-1)] is a
            # palindrome
            if (table[i + 1][j - 1] and
                    st[i] == st[j]):
                table[i][j] = True

                if k > maxLength:
                    start = i
                    maxLength = k
            i = i + 1
        k = k + 1

    print("start is: ",start)
    print("maxLength is : ",maxLength)
    print("start + maxLength: ",start + maxLength)

    print(st[start: start + maxLength])



# Driver program to test above functions
st = "cbbd"
l = longestPalSubstr(st)
