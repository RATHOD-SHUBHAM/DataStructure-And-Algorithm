# Tc: O(n) , all computation is done once
# Sc: O(n)
dic = {
        1: 0,
        2:1
      }
def getNthFib(n):
    # call the global dictionary
    global dic

    # check if n is present in dictionary
    if n in dic:
        return dic[n]
    else:
        # add it to dictionary
        dic[n] = getNthFib(n-1) + getNthFib(n-2)
        return dic[n]

    