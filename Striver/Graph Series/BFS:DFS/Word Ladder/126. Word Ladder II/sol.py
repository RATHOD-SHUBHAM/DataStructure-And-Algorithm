
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        visited = set()
        path = []
        
        # create a graph
        dic = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1 : ]
                dic[pattern].append(word)

        
        # BFS
        queue = [(beginWord, [beginWord])] # word, path
        visited.add(beginWord)

        while queue:
            # traverse till all the node at that level are exhausted
            q_len = len(queue)

            # nodes visietd in current level
            current_level_visited_node = set()

            for _ in range(q_len):
                word, sequence = queue.pop(0)

                if word == endWord:
                    path.append(sequence)
                    continue

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1 : ]

                    for nei in dic[pattern]:
                        if nei in visited:
                            continue
                        
                        new_sequence = sequence[:] + [nei]
                        queue.append((nei, new_sequence))

                        current_level_visited_node.add(nei)

            # we can add a word to visited, after every word from pervious level has finished exploring
            visited.update(current_level_visited_node)

        
        return path
