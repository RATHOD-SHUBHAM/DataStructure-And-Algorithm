def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False

    dp = [[False for _ in range(len(two) + 1)] for _ in range(len(one) + 1)]

    # when both the string are empty
    dp[0][0] = True

# ----------------------------------------------------------------
    
    # Row = 0
    for j in range(1, len(two) + 1):

        k = 0 + j - 1 # -1 for index at string 
        
        # check if the current element match and check the previous substring
        if two[j-1] == three[k] and dp[0][j - 1] == True:
                dp[0][j] = True

# ----------------------------------------------------------------
                
    # col = 0
    for i in range(1, len(one) + 1):

        k = i + 0 - 1 

        # compare the current values and check if the previous substring are true
        if one[i - 1] == three[k] and dp[i-1][0] == True:
                dp[i][0] = True

# ----------------------------------------------------------------

    # compare both the substring
    for i in range(1, len(one) + 1):
        for j in range(1, len(two) + 1):
            
            chose_1 = chose_2 = False

            k = i + j - 1 # -1 to get index from string three
            
            # check if string 1 match with string 3 check the substring match
            if one[i-1] == three[k] and  dp[i-1][j] == True:
                    chose_1 = True
                    
            # check if string 2 match with string 3 check if the susbtring match
            if two[j-1] == three[k] and dp[i][j-1] == True:
                    chose_2 = True


            # either one is true then pattern matches
            dp[i][j] = chose_1 or chose_2


    # this condition will give result of all substring
    return dp[-1][-1]
        
