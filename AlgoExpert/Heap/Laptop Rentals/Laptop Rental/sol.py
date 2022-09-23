def laptopRentals(times):
    # Write your code here.
    if len(times) == 0:
        return 0

    # sort based on start time
    times.sort(key = lambda x: x[0])

    # min heap
    laptop_heap = [times[0]]

    minHeap = heap(laptop_heap)

    for idx in range(1 , len(times)):
        currentInterval = times[idx]

        # check if the laptop can be rented to other student
        # if there is no overlap then remove the laptop from heap -- 
        # This means the laptop can be rented
        if minHeap.peek()[1] <= currentInterval[0]:
            minHeap.remove()

        minHeap.insert(currentInterval)

    # by the end we will have all user with their laptop count
    return len(laptop_heap)

class heap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        endIdx = len(array) - 1
        parentIdx = (endIdx - 1) // 2

        for idx in reversed(range(parentIdx + 1)):
            self.siftDown(idx , endIdx , array)

        return array

    def siftDown(self, currentIdx , endIdx, heap):
        childOneIdx = (currentIdx * 2) + 1

        while childOneIdx <= endIdx:
            childTwoIdx = (currentIdx * 2) + 2

            if childTwoIdx > endIdx:
                childTwoIdx = -1

            if childTwoIdx != -1 and heap[childTwoIdx][1] < heap[childOneIdx][1]:
                idxToswap = childTwoIdx
            else:
                idxToswap = childOneIdx

            if heap[idxToswap][1] < heap[currentIdx][1]:
                self.swap(idxToswap , currentIdx , heap)
                currentIdx = idxToswap
                childOneIdx = (currentIdx * 2) + 1
            else:
                return

    def siftUp(self, currentIdx , heap):
        parentIdx = (currentIdx - 1) // 2

        while currentIdx > 0 and heap[currentIdx][1] < heap[parentIdx][1]:
            self.swap(currentIdx , parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap)-1 , self.heap)
        valToremove = self.heap.pop()
        self.siftDown(0, len(self.heap)-1 , self.heap)
        return valToremove

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1 , self.heap)

    def swap(self, i, j ,heap):
        heap[i], heap[j] = heap[j] , heap[i]
