'''
295. Find Median from Data Stream
Hard

6999

132

Add to List

Share
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?


'''

class MedianFinder:

    def __init__(self):
        self.median = None
        
        self.lower = Heap(Max_Heap , []) # get the max number from the lower number range
        self.upper = Heap(Min_Heap , []) # get the min number from the upper number range
        
    # append the number to smaller bucket first then balance the bucket    
    def addNum(self, num: int) -> None:
        if not self.lower.length or num < self.lower.peek():
            self.lower.insert(num)
        else:
            self.upper.insert(num)
            
        self.rebalance()
        
        self.calMedian()
        
    # if there more number of number in one bucket compared to other    
    def rebalance(self):
        if self.lower.length - self.upper.length == 2:
            self.upper.insert(self.lower.remove())
        elif self.upper.length - self.lower.length == 2:
            self.lower.insert(self.upper.remove())
        else:
            pass
        
    def calMedian(self):
        # if even number of ele
        if self.lower.length == self.upper.length:
            self.median = (self.lower.peek() + self.upper.peek()) / 2
        # if odd number of ele
        elif self.lower.length > self.upper.length:
            self.median = self.lower.peek()
        else:
            self.median = self.upper.peek()

    def findMedian(self) -> float:
        return self.median

    
# heap builder
class Heap:
    def __init__(self, compareFunc , array):
        self.compareFunc = compareFunc
        self.heap = self.buildHeap(array)
        self.length = len(self.heap)
        
    def buildHeap(self,array):
        lastEleIdx = len(array) - 1
        parentIdx = lastEleIdx  // 2
        
        for currentIdx in reversed(range(parentIdx + 1)):
            self.siftDown(currentIdx , lastEleIdx , array)
            
        return array
    
    def siftDown(self, currentIdx , endIdx, heap):
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
        
        while currentIdx > 0 and self.compareFunc(heap[currentIdx], heap[parentIdx]):
            self.swap(currentIdx , parentIdx , heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2
            
    def peek(self):
        return self.heap[0]
    
    def remove(self):
        self.swap(0 , len(self.heap) - 1, self.heap)
        valToRemove = self.heap.pop()
        self.length -= 1
        self.siftDown(0 , len(self.heap) - 1, self.heap)
        return valToRemove
    
    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self.siftUp(len(self.heap) - 1 , self.heap)
        
        
    def swap(self, i , j , heap):
        heap[i] , heap[j] = heap[j] , heap[i]
        
def Max_Heap(a, b):
    return a > b

def Min_Heap(a, b):
    return a < b
    
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()