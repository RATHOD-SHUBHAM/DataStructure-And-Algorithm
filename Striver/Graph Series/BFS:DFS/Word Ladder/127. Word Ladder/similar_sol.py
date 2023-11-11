from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        
        dic = defaultdict(list)
        for word in wordList:
            w_len = len(word)
            
            for i in range(w_len):
                pattern = word[:i] + "*" + word[i+1:]
                
                dic[pattern].append(word)
                
        
        # print(dic)
        
        queue = [(beginWord, 1)]
        visited = set(beginWord)
        
        while queue:
            q_len = len(queue)
            
            for _ in range(q_len):
                
                word , level = queue.pop(0)

                if word == endWord:
                    return level

                w_len = len(word)
                
                for i in range(w_len):
                    pattern = word[:i] + "*" + word[i+1 : ]
                    
                    for nei in dic[pattern]:
                        if nei not in visited:
                            new_level = level + 1
                            queue.append([nei,new_level])
                            visited.add(nei)
                            
        return 0