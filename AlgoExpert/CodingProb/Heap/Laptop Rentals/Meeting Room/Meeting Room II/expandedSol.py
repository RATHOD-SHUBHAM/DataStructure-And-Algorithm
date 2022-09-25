# Time = O(nlogn)
# Sc = O(n)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return
        
        intervals.sort()
        
        min_no_of_room = [intervals[0]]
        
        minHeap = Heap(min_no_of_room)
        
        for i in range(1 , len(intervals)):
            cur_interval = intervals[i]
            
            if minHeap.peek()[1] <= cur_interval[0]:
                minHeap.remove()
                
            minHeap.insert(cur_interval)
            
        return len(min_no_of_room)
    
class Heap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)
        
    def buildHeap(self,array):
        lastEle = len(array) - 1
        parentIdx = (lastEle - 1) // 2
        
        for curIdx in reversed(range(parentIdx + 1)):
            self.siftDown(curIdx, lastEle, array)
            
        return array
    
    def siftDown(self, curIdx, endIdx, heap):
        childOneIdx = (curIdx * 2) + 1
        
        while childOneIdx <= endIdx:
            childTwoIdx = (curIdx * 2) + 2
            
            if childTwoIdx > endIdx:
                childTwoIdx = -1
                
            if childTwoIdx != -1 and heap[childTwoIdx][1] < heap[childOneIdx][1]:
                childToSwap = childTwoIdx
            else:
                childToSwap = childOneIdx
                
            if heap[childToSwap][1] < heap[curIdx][1]:
                self.swap(childToSwap, curIdx, heap)
                curIdx = childToSwap
                childOneIdx = (curIdx * 2) + 1
            else:
                return
            
    def siftUp(self, curIdx, heap):
        parentIdx = (curIdx - 1) // 2
        
        while curIdx > 0 and heap[curIdx][1] < heap[parentIdx][1]:
            self.swap(curIdx, parentIdx, heap)
            curIdx = parentIdx
            parentIdx = (curIdx - 1) // 2
            
    def peek(self):
        return self.heap[0]
    
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valToremove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valToremove
    
    def insert(self, val):
        self.heap.append(val)
        self.siftUp(len(self.heap) - 1, self.heap)
        
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j] , heap[i]