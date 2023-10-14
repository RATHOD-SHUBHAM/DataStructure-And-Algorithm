# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        # return type is a string
        string = ""
        string = self.DFS(root, string)

        # print(string)
        return string
    
    def DFS(self, root, string):
        if not root:
            string += 'None,' # careful if we add space, then while desrializing we will have to take care of None as well as (space)None
        else:
            string += str(root.val) + ','
            string = self.DFS(root.left, string)
            string = self.DFS(root.right, string)

        return string
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # print(data)
        data_list = data.split(',')
        # print(data_list)

        root = self.constructTree(data_list)

        return root
    
    def constructTree(self, data_list): 
        
        if data_list[0] == 'None':
            data_list.pop(0)
            return
        
        root_val = data_list.pop(0)
        root = TreeNode(root_val)

        root.left = self.construct(data_list)
        root.right = self.construct(data_list)

        return root

        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))