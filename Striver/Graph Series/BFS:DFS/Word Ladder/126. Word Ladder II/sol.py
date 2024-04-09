class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)

        graph = collections.defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[ : i] + '*' + word[i+1 : ]

                graph[pattern].append(word)
        
        queue = []
        queue.append([beginWord, [beginWord]]) # node and its sequence

        visited = set()
        visited.add(beginWord)

        output = []

        while queue:
            
            # This makes sure that the word is accessible by other words from same level
            neighbors_of_current_word = set() # keep track of neighbors visited by words of current level

            for _ in range(len(queue)):
                
                word , sequence = queue.pop(0)

                if word == endWord:
                    output.append(sequence)
                    continue

                for i in range(len(word)):
                    pattern = word[ : i] + '*' + word[i+1 : ]

                    for nei in graph[pattern]:
                        if nei in visited:
                            continue
                    
                        new_sequence = sequence[:] + [nei]
                        queue.append([nei, new_sequence])
                        neighbors_of_current_word.add(nei)
            
            # add the node to visited after all the words from current level have finished exploring the word
            visited.update(neighbors_of_current_word)
        
        return output