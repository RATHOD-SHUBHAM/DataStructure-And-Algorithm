def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False

    dp = [[False for _ in range(len(two) + 1)] for _ in range(len(one) + 1)]

    # when both the string are empty
    dp[0][0] = True

# ----------------------------------------------------------------
    
    # Row = 0
    for j in range(1, len(two) + 1):
        row = 0
        col = j - 1 # -1 for index in string 2
        
        k = row + col
        
        # check if the current element match
        if two[col] == three[k]:
            # check the previous substring
            if dp[0][j - 1] == True:
                dp[0][j] = True

# ----------------------------------------------------------------
                
    # col = 0
    for i in range(1, len(one) + 1):
        row = i - 1 # for index in string 1
        col = 0

        k = row + col

        # compare the current values
        if one[row] == three[k]:
            # check if the previous substring are true
            if dp[i-1][0] == True:
                dp[i][0] = True

# ----------------------------------------------------------------

    # compare both the substring
    for i in range(1, len(one) + 1):
        for j in range(1, len(two) + 1):
            
            chose_1 = chose_2 = False

            k = i + j - 1 # -1 to get index from string three
            
            # check if string 1 match with string 3
            if one[i-1] == three[k]:
                # check the substring match
                if dp[i-1][j] == True:
                    chose_1 = True
                    
            # check if string 2 match with string 3
            if two[j-1] == three[k]:
                # check if the susbtring match
                if dp[i][j-1] == True:
                    chose_2 = True


            # either one is true then pattern matches
            dp[i][j] = chose_1 or chose_2


    # this condition will give result of all substring
    return dp[-1][-1]
        
