from collections import defaultdict, Counter
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        visited = [False for _ in range(n)]
        lexiographical_str = ["0" for _ in range(n)]
        
        rechable_nei = self.get_rechable_nei(pairs)
        print(rechable_nei)
        
        for idx in range(n):
            if visited[idx]:
                continue
            
            rechable_idx = []
            self.get_rechable_idx(idx, rechable_idx, visited, rechable_nei)
            print(rechable_idx)
            rechable_idx.sort()
            
            # sort the character lexiographically at reachable idx
            sorted_char = []
            self.sort_char(s, sorted_char, rechable_idx)
            print(sorted_char)
            
            # replace char in main str
            self.replace_char(rechable_idx , lexiographical_str, sorted_char)
            
        return "".join(lexiographical_str)
            
        
    
    def get_rechable_nei(self, pairs):
        rechable_nei = defaultdict(list)
        
        for x , y in pairs:
            rechable_nei[x].append(y)
            rechable_nei[y].append(x)
        return rechable_nei
    
    def get_rechable_idx(self, cur_idx, rechable_idx, visited, rechable_nei):
        visited[cur_idx] = True
        rechable_idx.append(cur_idx)
        
        for nei in rechable_nei[cur_idx]:
            if not visited[nei]:
                self.get_rechable_idx(nei, rechable_idx, visited, rechable_nei)
                
    def sort_char(self, strs , sorted_char, rechable_idx):
        for idx in rechable_idx:
            char = strs[idx]
            sorted_char.append(char)
        return sorted_char.sort()
    
    def replace_char(self, rechable_idx , lexiographical_str, sorted_char):
        for idx in range(len(rechable_idx)):
            lexiographical_str[rechable_idx[idx]] = sorted_char[idx]