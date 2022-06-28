# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        # we need the max number for lower range number
        self.lower = Heap(MAX_HEAP , [])

        # we need min number for larger range number
        self.upper = Heap(MIN_HEAP , [])
        

    def insert(self, number):
        # Write your code here.
        #by default insert the first element in lower
        if not self.lower.length or number < self.lower.peek():
            self.lower.insert(number)
        else:
            self.upper.insert(number)


        # check for the balance
        self.rebalanceHeap()

        # calculate and update median
        self.calMedian()


    def rebalanceHeap(self):
        if self.lower.length - self.upper.length == 2:
            self.upper.insert(self.lower.remove())
        elif self.upper.length - self.lower.length == 2:
            self.lower.insert(self.upper.remove())
        else:
            pass

    def calMedian(self):
        if self.lower.length == self.upper.length:
            self.median = (self.lower.peek() + self.upper.peek()) / 2
        elif self.lower.length > self.upper.length:
            self.median = self.lower.peek()
        else:
            self.median = self.upper.peek()
        

    def getMedian(self):
        return self.median

class Heap:
    def __init__(self, compareFunc , array):
        self.compareFunc = compareFunc
        self.heap = self.buildHeap(array)
        self.length = len(self.heap)

    def buildHeap(self, array):
        lasteleIdx = len(array) - 1
        parentIdx = (lasteleIdx ) // 2

        for currentIdx in reversed(range(parentIdx + 1)):
            self.siftDown(currentIdx , lastEleIdx , array)

        return array

    def siftDown(self, currentIdx , endIdx , heap):
        childOneIdx = (currentIdx * 2) + 1

        while childOneIdx <= endIdx:
            childTwoIdx = (currentIdx * 2) + 2

            if childTwoIdx > endIdx:
                childTwoIdx = -1

            if childTwoIdx != -1 and self.compareFunc(heap[childTwoIdx] , heap[childOneIdx]):
                childToSwap = childTwoIdx
            else:
                childToSwap = childOneIdx

            if self.compareFunc(heap[childToSwap] , heap[currentIdx]):
                self.swap(childToSwap , currentIdx , heap)
                currentIdx = childToSwap
                childOneIdx = (currentIdx * 2) + 1
            else:
                return

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2

        while currentIdx > 0 and self.compareFunc(heap[currentIdx] , heap[parentIdx]):
            self.swap(currentIdx , parentIdx , heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0 , len(self.heap) - 1 , self.heap)
        valToremove = self.heap.pop()
        # decrease the length of the heap
        self.length -= 1
        self.siftDown(0 , len(self.heap) - 1 , self.heap)
        return valToremove

    def insert(self,value):
        self.heap.append(value)
        # increase the length
        self.length += 1
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i , j , heap):
        heap[i] , heap[j] = heap[j] , heap[i]

def MAX_HEAP(a , b):
    return a > b

def MIN_HEAP(a , b):
    return a < b