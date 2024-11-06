from typing import List

class Solution:
    def getPainters(self, area, boards, n):
        '''For the given area how many painters are needed'''
        no_of_painters = 1
        cur_area = 0

        for i in range(n):
            if cur_area + boards[i] <= area:
                cur_area += boards[i]
            else:
                cur_area = boards[i]
                no_of_painters += 1
        
        return no_of_painters


    def findLargestMinDistance(self, boards:List[int], k:int)->int:
        n = len(boards)

        if n < k:
            return -1
        
        # Assign range
        min_area = max(boards) # each painter can pick one board
        max_area = sum(boards) # one painters paints all board

        # each unit of a board takes 1 unit of time to paint.
        # 1 unit area = 1 unit time
        for area in range(min_area , max_area + 1):
            no_of_painters = self.getPainters(area, boards, n)

            if no_of_painters == k:
                return area



if __name__ == '__main__':
    ob = Solution()
    
    # Test case : 1
    # arr = [2, 1, 5, 6, 2, 3] 
    # k = 2

    # Test case : 2
    # arr = [10, 20, 30, 40]
    # k = 2

    # Test case : 3
    arr = [48, 90]
    k = 2

    result = ob.findLargestMinDistance(boards = arr, k = k)

    print("the area of the minimum time to get this job done: ", result)
