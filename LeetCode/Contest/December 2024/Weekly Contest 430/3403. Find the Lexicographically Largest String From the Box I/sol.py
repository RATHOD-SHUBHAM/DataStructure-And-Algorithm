class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1: 
            return word

        W = len(word)

        # Idea is to give everyone just one character and keep the max no of characters for one specific friend
        max_length = W - (numFriends - 1)

        options = []
        for i in range(W):
            # split_word = word[i: i + max_length]
            split_word = word[i: min(W, i + max_length)]
            options.append(split_word)

        options.sort()

        return options[-1]