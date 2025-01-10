# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # capture the state of string with each movement
        state_string = ""
        final_state = self.dfs(state_string, root)
        print(final_state)
        return final_state
    
    def dfs(self, state_string, root):
        if not root:
            state_string += 'None' + ','
            return state_string
        
        state_string += str(root.val) + ','

        # Update the state
        new_state_string = self.dfs(state_string, root.left)
        final_state_string = self.dfs(new_state_string, root.right)

        return final_state_string

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nums = data.split(',')
        return self.construct_tree(nums)

    def construct_tree(self, nums):
        if nums[0] == 'None':
            nums.pop(0)
            return
        
        root_val = nums.pop(0)
        root = TreeNode(root_val)


        # Move left
        root.left = self.construct_tree(nums)
        root.right = self.construct_tree(nums)

        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))