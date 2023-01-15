class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        
        # for every parent - add the child
        tree = {}
        for i in range(1, n):
            if parent[i] not in tree:
                tree[parent[i]]=[i]
            else:
                tree[parent[i]].append(i)
                
        # print(tree)
            
        # longest path for 1 node is 1
        longest_path = [1]
        root = 0
        self.dfs(root, tree, s, longest_path)
        return longest_path[0]
    
    def dfs(self, root, tree, s, longest_path):
        # check if the given root is parent - except leaf node everything else is parent
        # if leaf node - return 1
        if root not in tree:
            return 1

        # keep track of longest path for the current node
        cur_longest_path = 1

        for child in tree[root]:

            # get the longest path of the child
            child_path = self.dfs(child, tree, s, longest_path)

            # when the values are differnet
            if s[root] != s[child]:
                # get the longest path by cehcking the left adn right child value
                longest_path[0] = max(longest_path[0] , child_path + cur_longest_path)
                # update the longest path for current node
                cur_longest_path = max(cur_longest_path , child_path + 1 )

        return cur_longest_path