class Solution:
    def findCeil(self,root, inp):
        # code here
        curNode = root
        ceil = -1
        
        while curNode:
            if curNode.key == inp:
                ceil = curNode.key
                break
            elif curNode.key < inp:
                curNode = curNode.right
                
            elif curNode.key > inp:
                ceil = curNode.key
                curNode = curNode.left
                    
        return ceil