# -------------- Brute Force ----------------

# Flatten Tree + Two Sum.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.inorder = []
        self.dic = {}

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.inorderTraversal(root)
        # print(self.inorder)
        return self.twoSum(k)
    
    def inorderTraversal(self,root):
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()
            self.inorder.append(node.val)

            root = node.right
        
        return

    def twoSum(self, k):
        n = len(self.inorder)

        for i in range(n):
            num = self.inorder[i]

            diff = k - num

            if diff in self.dic:
                return True
            
            self.dic[num] = i
        
        return False
        
# -------------- Dynamic Fetching ----------------

# Flatten Tree + Two Sum.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.stack = []
        self.dic = {}

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.inorderTraversal(root)
        return self.twoSum(k)
    
    def inorderTraversal(self,root):
        while root:
            self.stack.append(root)
            root = root.left
        return

    def twoSum(self, k):
        while self.stack:
            node = self.stack.pop()
            num = node.val

            diff = k - num

            if diff in self.dic:
                return True
            
            self.dic[num] = num

            if node.right:
                self.inorderTraversal(node.right)
    
        return False

# -------------- Dynamic Fetching with Set ----------------

# Flatten Tree + Two Sum.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.stack = []
        self.dic = set()

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.inorderTraversal(root)
        return self.twoSum(k)
    
    def inorderTraversal(self,root):
        while root:
            self.stack.append(root)
            root = root.left
        return

    def twoSum(self, k):
        while self.stack:
            node = self.stack.pop()
            num = node.val

            diff = k - num

            if diff in self.dic:
                return True
            
            self.dic.add(num)

            if node.right:
                self.inorderTraversal(node.right)
    
        return False
    
