# Time = O((4^n) *n) # atmost 4 calls will be present in stack 
# Space = O((4^n) *n)

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
    curList = [0] * len(phoneNumber)
	finalList = []
	
	helper(0,phoneNumber,curList,finalList)
	
	return finalList


def helper(idx,phoneNumber,curList,finalList):
	if idx >= len(phoneNumber):
		curString = ''.join(curList) # O(n)
		finalList.append(curString)
		
	else:
		curDigit = phoneNumber[idx]
		letters = dic[curDigit]
		
		for letter in letters:
			curList[idx] = letter
			helper(idx + 1 ,phoneNumber,curList,finalList)