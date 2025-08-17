class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # Check if end word exist
        if endWord not in wordList:
            return []

        # Pattern-Based Graph Construction
        wordList.append(beginWord)
        
        graph = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[ : i] + "*" + word[i+1: ]
                graph[pattern].append(word)
        
        # BFS For Shortest Path
        queue = collections.deque()
        visited = set()

        queue.append((beginWord, [beginWord]))
        visited.add(beginWord)

        op = []

        while queue:
            # Same node can be neighbor for multiple word, so keep track locally
            current_visited = set() # This makes sure that the word is accessible by other words from same level

            # If there are multiple element in the queue, then they are on same level
            for _ in range(len(queue)):
                word, seq = queue.popleft()

                if word == endWord:
                    op.append(seq)
                    continue

                for i in range(len(word)):
                    pattern = word[ : i] + "*" + word[i+1: ]

                    for nei in graph[pattern]:
                        if nei in visited:
                            continue

                        new_seq = seq[:] + [nei]
                        queue.append((nei, new_seq))
                        current_visited.add(nei)
            
            # Prevents looping the nodes on same level
            visited.update(current_visited)
        
        return op