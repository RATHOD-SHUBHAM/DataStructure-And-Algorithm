from collections import defaultdict
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # appending begin word to wordlist to find its neighbor
        wordList.append(beginWord)
        
        # creating adjacency list
        dic = defaultdict(list) #initializing it with list
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1 : ]
                dic[pattern].append(word)
                
        # print(dic)
        
        # BFS -> through every patterns neighbor
        visited = set(beginWord) #keep track of visited node
        q = deque([beginWord])
        Level = 1 # 1 becasue we might have direct step for beginWord to endWord
        
        while q:
            # print("q is: ",q)
            for i in range(len(q)):
                word = q.popleft()
                # print("word is: ",word)
                if word == endWord:
                    return Level
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1 : ]
                    
                    for neighbor in dic[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
            Level += 1
            
        return 0
        
        