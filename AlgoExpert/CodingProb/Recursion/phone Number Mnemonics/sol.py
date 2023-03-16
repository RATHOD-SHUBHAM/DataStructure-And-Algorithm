# Tc and Sc: O((4^n) * n )
dic = {
	"0" : ["0"],
	"1" : ["1"],
	"2" : ["a","b","c"],
	"3" : ["d","e","f"],
	"4" : ["g","h","i"],
	"5" : ["j","k","l"],
	"6" : ["m","n","o"],
	"7" : ["p","q","r","s"],
	"8" : ["t","u","v"],
	"9" : ["w","x","y","z"]
}


def phoneNumberMnemonics(phoneNumber):
    mnemonics = []
    cur_combination = []
    idx = 0
    # O(n) : call for n digit
    return mnemonic(idx, phoneNumber , cur_combination, mnemonics)

# dfs
def mnemonic(idx , phoneNumber , cur_combination, mnemonics):
    # base case
    if idx >= len(phoneNumber):
        # Sc: O(4^n) : each digit will add max 4 element
        lst_to_str = "".join(cur_combination) # O(n) space
        mnemonics.append(lst_to_str)
        return mnemonics

    # get the words associcated with current element
    cur_digit = phoneNumber[idx]
    letters = dic[cur_digit]

    #pick up each letter and then make a new combination
    # O(4 ^ n) : max we will have 4 letter
    for letter in letters:
        cur_combination.append(letter)
        mnemonic(idx + 1 , phoneNumber , cur_combination, mnemonics)
        cur_combination.pop()

    return mnemonics
