class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        
        dic = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y","z"]
        }
        
        mnemonics = []
        cur_combination = []
        idx = 0
        return self.mnemonic(idx, dic, digits, cur_combination, mnemonics)
    
    def mnemonic(self, idx, dic, digits, cur_combination, mnemonics):
        # base case
        if idx >= len(digits):
            lst_to_str = "".join(cur_combination)
            mnemonics.append(lst_to_str)
            return mnemonics
        
        # dfs
        cur_digit = digits[idx]
        letters = dic[cur_digit] # get the words associated with each digit
        
        # iterate over each letter and form combination with every other letter
        for letter in letters:
            cur_combination.append(letter)
            self.mnemonic(idx + 1, dic, digits, cur_combination, mnemonics)
            cur_combination.pop()
        
        return mnemonics


# ------------------------------------------------------------------------------------
    
# Global variables
    
class Solution:
    def __init__(self):
        self.mnemonics = []
        
        self.dic = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y","z"]
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        cur_combination = []
        idx = 0
        self.backTrack(idx, cur_combination, digits)

        return self.mnemonics

    def backTrack(self, idx, cur_combination, digits):
        
        if idx >= len(digits):
            val = "".join(cur_combination)
            self.mnemonics.append(val)
            return
        
        cur_digit = digits[idx]
        letters = self.dic[cur_digit]

        for letter in letters:
            cur_combination.append(letter)
            self.backTrack(idx + 1, cur_combination, digits)
            cur_combination.pop()
        
        return