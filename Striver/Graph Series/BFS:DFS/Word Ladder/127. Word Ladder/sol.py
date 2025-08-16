class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Check if end word exist
        if endWord not in wordList:
            return 0

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

        level = 1 # Level tracking

        queue.append((beginWord , level))
        visited.add(beginWord)

        while queue:
            word, level = queue.popleft()

            if word == endWord:
                return level
            
            for i in range(len(word)):
                pattern = pattern = word[ : i] + "*" + word[i+1: ]

                for nei in graph[pattern]:
                    if nei in visited:
                        continue
                    
                    queue.append((nei, level + 1))
                    visited.add(nei)
        

        return 0