class MyHashSet:

    def __init__(self):
        self.hashing_value = 769 # 769 is a arbitary prime number. We can choose any prime number
        
        # create a bucket
        self.bucketList = [Bucket() for i in range(self.hashing_value)]
        
        

    def add(self, key: int) -> None:
        # get the Index to store value in bucket. By hashing the key with length of bucket
        hash_index = self.hash_function(key)
        
        # add the key at that particular hash_idex of the bucket
        self.bucketList[hash_index].insert(key) 
        

    def remove(self, key: int) -> None:
        # remove key from particular index
        remove_index = self.hash_function(key)
        
        # remove from that particular index of the bucket
        self.bucketList[remove_index].delete(key)
        

    def contains(self, key: int) -> bool:
        # look at that particular index if value is present
        search_index = self.hash_function(key)
        
        # return of the key is present
        return self.bucketList[search_index].search(key)
        
    def hash_function(self, key):
        hashing_index = key % self.hashing_value
        return hashing_index
        
        
class Bucket:
    def __init__(self):
        # make a call to binary search tree
        self.tree = BST()
        
    def insert(self, key):
        # insert a the current key value for a particular node
        self.tree.root = self.tree.insertBST(self.tree.root, key)
        
    def delete(self, key):
        # for a particular root node perform delete operation
        self.tree.root = self.tree.deleteBST(self.tree.root, key)
        
        
    def search(self, key):
        # return if the key exist
        return self.tree.searchBST(self.tree.root, key) is not None
    

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class BST:
    def __init__(self, root = None):
        self.root = root
        
        
    def searchBST(self, root, val):
        while root is not None and val != root.val:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
                
        return root
    
    def insertBST(self, root, val):
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertBST(root.left, val)
        elif val > root.val:
            root.right = self.insertBST(root.right, val)
        
        return root

    
    def deleteBST(self, root, val, parentNode = None):
        curNode = root
        
        
        while curNode:
            # perform searching
            if val < curNode.val:
                parentNode = curNode
                curNode = curNode.left
            elif val > curNode.val:
                parentNode = curNode
                curNode = curNode.right
            else:
                # node is found
                # case 1 : 2 child are present
                if curNode.left and curNode.right:
                    curNode.val = self.getMin(curNode.right)
                    self.deleteBST(curNode.right, curNode.val, curNode)
                    
                else:
                    # parent Not found
                    if not parentNode:
                        if curNode.left:
                            curNode.val = curNode.left.val
                            curNode.right = curNode.left.right
                            curNode.left = curNode.left.left
                        elif curNode.right:
                            curNode.val = curNode.right.val
                            curNode.left = curNode.right.left
                            curNode.right = curNode.right.right
                        # if there is no parent and no child
                        else:
                            return
                        
                    elif parentNode.left == curNode:
                        parentNode.left = curNode.left if curNode.left else curNode.right
                    
                    elif parentNode.right == curNode:
                        parentNode.right = curNode.right if curNode.right else curNode.left
                        
                    break
                    
        return root
    
    def getMin(self, node):
        curNode = node
        
        while curNode.left:
            curNode = curNode.left
            
        return curNode.val
    

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)