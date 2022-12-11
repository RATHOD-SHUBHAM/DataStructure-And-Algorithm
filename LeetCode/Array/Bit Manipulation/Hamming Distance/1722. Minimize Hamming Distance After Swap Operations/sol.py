# Tc: O(n + edges) | Sc: O(n)

from collections import Counter, defaultdict
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        minimum_hamming_distance = 0
        
        # keep track of visited index
        visited = [False for _ in range (n)]
        
        reachable_neighbor = self.getNeighbor(allowedSwaps)
        print("reachable_neighbor: ",reachable_neighbor)
        
        # got through every index and compare the values
        for idx in range(n):
            # if the index has been previously compared just continue
            if visited[idx]:
                continue
            
            # get all the indexs that can be reached from current idx
            reachable_idx = []
            self.get_rechable_idx(idx, visited, reachable_idx, reachable_neighbor)
            
            # compare the value at cur idx and its rechable idx
            dist = self.manhatten_dist(reachable_idx, source, target)
            
            # combine all the differences
            minimum_hamming_distance += dist
            
        return minimum_hamming_distance
            
            
    # map every ele to its neighbor
    def getNeighbor(self,allowedSwaps):
        reachable_neighbor = defaultdict(list)
        for x, y in allowedSwaps:
            reachable_neighbor[x].append(y)
            reachable_neighbor[y].append(x)
        return reachable_neighbor
    
    # for the cur idx get the neighbor from the mapping
    def get_rechable_idx(self, cur_idx, visited, reachable_idx, reachable_neighbor):
        print("cur_idx: ",cur_idx)
        # mark the cur index as visited
        visited[cur_idx] = True
        print("visited: ",visited)
        # make it reachable
        reachable_idx.append(cur_idx)
        print("reachable_idx: ",reachable_idx)
        
        # get the neighbors
        for nei in reachable_neighbor[cur_idx]:
            print("nei: ",nei)
            # if the node has been visited then dont : it will cause unnecessay loop
            if not visited[nei]:
                self.get_rechable_idx(nei, visited, reachable_idx, reachable_neighbor)

    
    # compare the values at the indexes
    # even after interchanging at particular index. count should remain same for the elemenets
    def manhatten_dist(self, indexes, source, target):
        diff = 0
        source_target_diff = 0 # how many elements are different from source
        target_source_diff = 0 # how many elements are different from target
        
        source_counter = Counter()
        target_counter = Counter()
        
        # count the numbers
        for index in indexes:
            source_counter[source[index]] += 1
            target_counter[target[index]] += 1
        
        # sum of surce and target and then their difference
        source_target_diff = (source_counter - target_counter).total()
        target_source_diff = (target_counter - source_counter).total()
        
        # get the total difference 
        diff += (source_target_diff + target_source_diff) // 2
        
        return diff
            
            