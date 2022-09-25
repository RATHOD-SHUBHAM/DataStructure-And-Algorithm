# element is "at most" k position away from its sorted position
# TC : O(n) for every index
# TC: O(log k) because we will have at most k + 1 element in heap
# therefore TC: O(nlogk)
# Sc: O(k). We will have k + 1 element in heap, and for we array we sort inplace

def sortKSortedArray(array, k):
    # Write your code here.
    # create a min heap starting from 0 to k+1. if k+1 is greater than len then create min heaq 0 to len
    MinHeap = Heap( array[: min( k + 1 , len(array) ) ])

    # correct index where the ele needs to be appended
    nextIdx = 0

    for idx in range(k + 1 , len(array)):
        # remove the smallest ele
        eleToAppend = MinHeap.remove()
        # add the ele in correct place
        array[nextIdx] = eleToAppend

        nextIdx += 1

        # now include the next element in heap
        MinHeap.insert(array[idx])

    # now check if there are any elements that are left in heap 
    while not MinHeap.isEmpty():
        # remove the smallest ele
        eleToAppend = MinHeap.remove()
        # add the ele in correct place
        array[nextIdx] = eleToAppend

        nextIdx += 1

    return array


class Heap:
    def __init__(self,array):
        self.heap = self.buildHeap(array)

    def isEmpty(self):
        return len(self.heap) == 0

    def buildHeap(self,array):
        lastEleIdx = len(array) - 1
        parentIdx = lastEleIdx // 2

        for currentIdx in reversed(range(parentIdx + 1)):
            self.siftDown(currentIdx , lastEleIdx , array)

        return array

    def siftDown(self, currentIdx , endIdx , heap):
        childOneIdx = (currentIdx * 2) + 1

        while childOneIdx <= endIdx:
            childTwoIdx = (currentIdx * 2) + 2

            if childTwoIdx > endIdx:
                childTwoIdx = -1

            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                childToSwap = childTwoIdx
            else:
                childToSwap = childOneIdx

            if heap[childToSwap] < heap[currentIdx]:
                self.swap(childToSwap , currentIdx , heap)
                currentIdx = childToSwap
                childOneIdx = (currentIdx * 2) + 1
            else:
                return

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2

        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2


    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valToremove = self.heap.pop()
        self.siftDown(0 , len(self.heap) - 1, self.heap)
        return valToremove

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1 , self.heap)

    def swap(self, i , j , heap):
        heap[i] , heap[j] = heap[j] , heap[i]

