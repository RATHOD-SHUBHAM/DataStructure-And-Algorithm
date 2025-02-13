class Solution:
    def createTree(self, root, l):
        # Code here
        n = len(l)
        
        idx = 1
        queue = [root]
        
        while stack:
            node = queue.pop(0)
            
            if idx < n:
                cur_val = l[idx]
                node.left = Node(cur_val)
                queue.append(node.left)
            else:
                break
            
            
            idx += 1
            
            if idx < n:
                cur_val = l[idx]
                node.right = Node(cur_val)
                queue.append(node.right)
            else:
                break
            
            idx += 1
        
        return root