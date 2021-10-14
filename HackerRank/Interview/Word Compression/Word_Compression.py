def CompressWord(word,k):
    
    # creating an empty list
    my_list = []

    for character in word:
        # last element's first character in my_list is same as the character 
        if my_list and my_list[-1][0] == character:
            # print("char is",character)
            # print("my list",my_list)
            # print(my_list[-1][0])
            
            my_list[-1][1] += 1

            if my_list[-1][1] == k:
                my_list.pop()

        else:
            my_list.append([character,1])
            
    print("list",my_list)

    output = ''

    for character,count in my_list:
        print("Charcter is: ",character)
        print("count is : ",count)
        output += character * count # a * 2 = aa

    return output
    




if __name__ == '__main__':
    print("Compressed Word is: ",CompressWord("abbcccb",3))
    print("Compressed Word is: ",CompressWord("aba",2))
    print("Compressed Word is: ",CompressWord("aba",2))
    print("Compressed Word is: ",CompressWord("aaba",3))