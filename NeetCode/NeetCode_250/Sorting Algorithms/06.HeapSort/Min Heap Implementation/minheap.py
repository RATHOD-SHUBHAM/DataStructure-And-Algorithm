'''
Formula: 
ChildOne = 2i + 1
ChildTwo = 2i + 2
Parent = (i-1)/2

Insert = Insert at the last 
and shift up

Remove = We can only remove the root node of a heap (Either max number or min number)
Swap the root with last element
Pop out the last element
Shift down

Build = Loop(
	Start at the last parent node
	Shift down
)


# Run time

Shift up and shift down = O(log(n))
n = number of elements in the array

Inserting and Removal = O(log(n))
because shift up and shift down both are dependent on Shift up and Shift down

Build Heap = O(n)

O(n) if we use shift down to build the heap
O(n log(n)) if we use shift up to build the heap

'''


# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        lastEle = len(array) - 1
        parentIdx = (lastEle - 1) // 2
		# print(parentIdx)
       
        for currentIdx in reversed(range(parentIdx+1)):
			# print(currentIdx)
            self.siftDown(currentIdx,len(array) - 1,array) 
        return array
		

    def siftDown(self, currentIdx, endIdx, heap):
        # calculate child
        childOneIdx = (currentIdx * 2) + 1
		# Check if the child is the leaf and exist
        while childOneIdx <= endIdx:
			# if there is no first child then for sure there will not be second child
			# if ((currentIdx * 2) + 2) <= endIdx:
			# 	childTwoIdx = (currentIdx * 2) + 2
			# else:
			# 	childTwoIdx = -1
			
            childTwoIdx = (currentIdx * 2) + 2
            if childTwoIdx > endIdx:
                childTwoIdx = -1
				
			# check if child two is smaller than child one and parent
			
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                childToSwap = childTwoIdx
            else:
                childToSwap = childOneIdx
				
                
            if heap[childToSwap] < heap[currentIdx]:
                self.swap(currentIdx,childToSwap, heap)
                currentIdx = childToSwap
                childOneIdx = (currentIdx * 2) + 1
            else:
                # if there are no elements to swap --> just break
                break

    def siftUp(self,currentIdx):
		# Find the parent element Index
        parentIdx = (currentIdx - 1) // 2
		# check if we are in the indexLimit and not the root element and if the current element is smaller than the parent element then we swap
        while parentIdx >= 0 and self.heap[currentIdx] < self.heap[parentIdx]:
            self.swap(parentIdx, currentIdx,self.heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2 # once we reach the root or our elements are heapified then we break out of the loop 

    def peek(self):
        return self.heap[0]

    def remove(self):
        # Swap the root with last element
        firstIdx = 0
        endIdx = len(self.heap) - 1
        self.swap(firstIdx, endIdx, self.heap)
        
        # Pop out the last element
        valToRemove = self.heap.pop()
		
        # shift down from the top until last element
        endIdx = len(self.heap) - 1
        self.siftDown(0,endIdx,self.heap)
        return valToRemove

    def insert(self, value):
        # Append the value to the end of heap
        self.heap.append(value)
        # Shift the value up to its right place
        endIdx = len(self.heap) - 1
        self.siftUp(endIdx)
		
    def swap(self,i,j,heap):
        heap[i] , heap[j] = heap[j] , heap[i]


if __name__ == "__main__":
    	# Test cases
        minHeap = MinHeap([ 4, 10, 3, 5, 1 ])
        minHeap.insert(3)
        minHeap.insert(1)
        minHeap.insert(2)
        # [1,3,2]
        print(minHeap)
        # 1
        print(minHeap.peek())
        # 1
        print(minHeap.remove())
        # 2
        print(minHeap.remove())
        # 3
        print(minHeap.remove())
        minHeap.insert(4)
        minHeap.insert(5)
        # [4,5]
        print(minHeap)