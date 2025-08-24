class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)

        # Step 1: Build the graph
        graph = {} # This will help us to know if there are independent letters
        indegree = {}

        for word in words:
            for letter in word:
                graph[letter] = []
                indegree[letter] = 0


        """
        In lexicographic (dictionary) ordering, when comparing two words:
        1. Compare characters position by position from left to right
        2. If all compared characters are equal AND one word is shorter, the shorter word comes first

        """

        for i in range(n-1):
            word_1 = words[i]
            word_2 = words[i+1]
            
            # This will be used to check if first word is smaller than second word
            smaller_word = min(word_1, word_2)

            ns = len(smaller_word)

            # Rule 1: Compare character by characters
            for j in range(ns):
                letter_1 = word_1[j]
                letter_2 = word_2[j]

                if letter_1 != letter_2:
                    graph[letter_1].append(letter_2)
                    break # No further comparison is needed
                else:
                    # Rule 2: Make sure the shorter word comes before the larger word
                    if j == ns-1 and len(word_1) > len(word_2):
                        return ""

        # Step 2: Get the order of words -> Khans Algorithm
        m = len(graph)
        
        for key, value in graph.items():
            for letter in value:
                indegree[letter] += 1


        queue = collections.deque()
        for key, value in indegree.items():
            if value == 0:
                queue.append(key)
        
        count = 0
        topo_sort = []
        while queue:
            node = queue.popleft()

            for nei in graph[node]:
                indegree[nei] -= 1
                
                if indegree[nei] == 0:
                    queue.append(nei)
                    
            count += 1
            topo_sort.append(node)
    

        if count == m:
            return "".join(topo_sort)
        else:
            return ""