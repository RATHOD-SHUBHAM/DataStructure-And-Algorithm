class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # base case
        if len(word) == 1:
            return True
        
        # when starting word is capital
        if word[0].isupper():
            # if 2nd word is also capital - then eveything else should be captial
            if word[1].isupper():
                return word == word.upper()
            # else every thing else should be lower
            else:
                return word[1: ] == word[1: ].lower()
        # if the start is itself lower
        else:
            return word == word.lower()