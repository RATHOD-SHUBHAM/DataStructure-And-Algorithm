from collections import defaultdict, Counter
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        op = [0] * n
        
        adj_lst = defaultdict(list)
        
        for parent, child in edges:
            adj_lst[parent].append(child)
            adj_lst[child].append(parent)
            
        root = 0
        parentNode = -1
        
        self.dfs(root, parentNode, adj_lst, op, labels)
        
        return op
    
    def dfs(self, node, parentNode, adj_lst, op, labels):
        freq_counter = Counter() # get the count of character for cur node
        
        for nei in adj_lst[node]:
            # avoid visiting parent node
            if nei == parentNode:
                continue
                
            # add the freq_count of the child nodes
            freq_counter += self.dfs(nei, node, adj_lst, op, labels)
            
            
        # increase the freq of current node
        nodes_label = labels[node]
        freq_counter[nodes_label] += 1
        
        op[node] = freq_counter[nodes_label]
        
        # return the counter
        return freq_counter
            
        