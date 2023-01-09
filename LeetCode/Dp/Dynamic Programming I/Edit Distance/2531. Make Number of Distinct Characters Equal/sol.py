from collections import Counter
class Solution:
    def insertAndRemove(self, word_counter, char_to_insert, char_to_remove): 
        word_counter[char_to_insert]+=1
        word_counter[char_to_remove]-=1
        
        if(word_counter[char_to_remove]==0):
            del word_counter[char_to_remove]     #if freq of that char reaches zero, then remove the key from dict
        
        
    def isItPossible(self, word1: str, word2: str) -> bool:
        
        word1_counter = Counter(word1)
        word2_counter = Counter(word2)

            
        # print(word1_counter)
        # print(word2_counter)

        # if i use len of input: run time will be O(n^2) - as the size opf ip increases the run time may increase or decrese
        # O(26) - constant run time
        # no matter my input - run time will stay constant    
        for c1 in string.ascii_lowercase:         # this for loop iterates through c1='a' to c1='z'
            if c1 not in word1_counter:  # if the char is not present then skip
                    continue
            # print(c1)
            for c2 in string.ascii_lowercase:     # this for loop iterates through c2='a' to c2='z'
                
                if c2 not in word2_counter:  # if the char is not present then skip
                    continue
                
                # swap
                self.insertAndRemove(word1_counter, c2, c1); # insert c2 to word1 and remove c1 from word1
                self.insertAndRemove(word2_counter, c1, c2); # insert c1 to word2 and remove c2 from word2
                # print("\n")
                # print(word1_counter)
                # print(word2_counter)
                
                # count the number of unique character
                # the character need not bee the same but just the number of unique character need to be same
                if len(word1_counter)== len(word2_counter):  # if size of both dicts are equal then possible return true
                    return True
				
                # reset back the maps - swap back
                self.insertAndRemove(word1_counter, c1, c2); # insert c1 back to word1 and remove c2 from word1         
                self.insertAndRemove(word2_counter, c2, c1); # insert c2 back to word2 and remove c1 from word2                
        return False