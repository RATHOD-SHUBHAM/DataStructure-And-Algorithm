def longestStringChain(strings):
    strings.sort(key = lambda x : len(x))

    cache = {}
    for string in strings:
        cache[string] = {
            "previousString" : None,
            "stringChainLen" : 1
        }

    # divide the string into smaller chunk and check if they are present in the cache
    for string in strings:
        findLongestChain(string, cache)


    # get the string with maximum len string chain
    maxLenString = findMaxLenStringChain(cache, strings)

    # build the subsequence
    return buildSequence(strings, cache, maxLenString) 


def findLongestChain(string, cache):

    for i in range(len(string)):
        smallString = getSmallerString(i, string)

        if smallString not in cache:
            continue

        updateCache(string, smallString, cache)

def getSmallerString(i, string):
    return string[ : i] + string[i+1 : ]

def updateCache(string, smallString, cache):
    stringChain_len_of_smallString = cache[smallString]["stringChainLen"]
    stringChain_len_of_string = cache[string]["stringChainLen"]

    if stringChain_len_of_smallString + 1 > stringChain_len_of_string:
        cache[string] = {
                "previousString" : smallString,
                "stringChainLen" : stringChain_len_of_smallString + 1
            }  

def findMaxLenStringChain(cache, strings):
    maxChainLen = 0
    maxLenString = None

    for string in strings:
        if cache[string]["stringChainLen"] > maxChainLen:
            maxChainLen = cache[string]["stringChainLen"]
            maxLenString = string

    return maxLenString


def buildSequence(strings, cache, maxLenString):
    seq = []

    currentStr = maxLenString

    while currentStr is not None:
        seq.append(currentStr)

        currentStr = cache[currentStr]["previousString"]

    return seq if len(seq) > 1 else []