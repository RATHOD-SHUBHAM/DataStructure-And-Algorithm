class Solution:
    def floor(self, root, x):
        flr = -1
        node = root
        
        while node:
            if node.data == x:
                flr = node.data
                break
            elif node.data > x:
                node = node.left
            else:
                flr = node.data
                node = node.right
        
        return flr