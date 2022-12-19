'''
We want to find all the possible ways of arranging 2 boys and 1 girl on 3 benches. Constraint: Girl should not be on the middle bench.

'''
class solution:
    def combination(self, array):
        subset = []
        cur_set = []
        idx = 0
        return self.subsets(idx, array, subset, cur_set)

    def subsets(self, idx, array, subset, cur_set):
        # base case
        if idx >= len(array):
            subset.append(cur_set[:])
            return subset
        
        #decision1: add the current element
        cur_set.append(array[idx])
        self.subsets(idx + 1, array, subset, cur_set)

        # decision 2: dont add the current ele
        cur_set.pop()
        self.subsets(idx + 1, array, subset, cur_set)

        return subset


if __name__ == '__main__':
    Sol = solution()
    array = ["b1" , "b2", "g1"]
    print(Sol.combination(array))
