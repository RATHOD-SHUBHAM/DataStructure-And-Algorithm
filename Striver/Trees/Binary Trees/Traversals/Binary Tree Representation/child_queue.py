class Solution:
    def createTree(self, root, l):
        # Code here
        n = len(l)
        
        queue = [(root, 0)]
        
        while queue:
            node, i = queue.pop(0)
            
            first_child_idx = (2 * i) + 1
            
            if first_child_idx < n:
                node.left = Node(l[first_child_idx])
                queue.append((node.left, first_child_idx))
                
                
                second_child_idx = (2 * i) + 2
                
                if second_child_idx < n:
                    node.right = Node(l[second_child_idx])
                    queue.append((node.right, second_child_idx))
                else:
                    break
            
            else:
                break
        
        return root