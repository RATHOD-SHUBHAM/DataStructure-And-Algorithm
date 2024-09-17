'''
Steps:

a = a ^ b

b = a ^ b = (a ^ b) ^ b = a
ie b = a

a = a ^ b = (a ^ b) ^ b = (a ^ b) ^ a = b
ie a = b


'''
class Solution:
    def get(self, a, b):
        #code here
        a = a ^ b
        
        b = a ^ b
        
        a = a ^ b
        
        return a , b