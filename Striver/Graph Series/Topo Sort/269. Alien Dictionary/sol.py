class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)
        
        # ------------------- Build and Define Graph --------------
        
        # get the individual nodes and mark the default node value as 0
        graph = {}
        indegree = {}
        for word in words:
            for letter in word:
                graph[letter] = []
                indegree[letter] = 0
        
        # print(graph)
        # print(indegree)
        
        # build the graph -> connect the nodes
        for i in range(n-1):
            word_1 = words[i]
            word_2 = words[i+1]
            
            # compare each word letter by letter
            smaller_word = min(word_1 , word_2)
            ns = len(smaller_word)
            
            for j in range(ns):
                letter_1 = word_1[j]
                letter_2 = word_2[j]
                
                # if two letters are not same, we found a edge
                if letter_1 != letter_2:
                    graph[letter_1].append(letter_2)
                    break # no need to compare any further
                else:
                    # if we have reached the end, and if word 1 is greater than word 2 then it doesnot match the lexicographically ordering
                    if j == ns - 1:
                        if len(word_1) > len(word_2):
                            return ""
                
        # print(graph)
        
        # ------------------------ Topological Sort -> Kahns Algorithm ----------------------
        
        # get indegree.
        for node in graph:
            for child in graph[node]:
                indegree[child] += 1
        
        # print("indegree: ", indegree)
        
        # add the items in queue
        queue = []
        for parent, child in indegree.items():
            if child == 0:
                queue.append(parent)
        
        # print(queue)
        
        # pop the element from queue and reduce the indegree of neighbor
        topo_sort = []
        count = 0
        
        while queue:
            node = queue.pop(0)
            
            for nei in graph[node]:
                indegree[nei] -= 1
                
                if indegree[nei] == 0:
                    queue.append(nei)
                    
            count += 1
            topo_sort.append(node)
            
            
        # print("topo_sort : ", topo_sort)
        
        if count == len(graph):
            return "".join(topo_sort)
        else:
            return ""