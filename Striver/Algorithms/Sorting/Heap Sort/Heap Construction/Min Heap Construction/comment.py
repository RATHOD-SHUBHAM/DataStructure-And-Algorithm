'''
Formula: 
if CurNode = i
    ChildOne = 2i + 1
    ChildTwo = 2i + 2
    Parent = (i-1)/2



# Run time

Shift up and shift down = O(log(n))
n = number of elements in the array

Inserting and Removal = O(log(n))
because shift up and shift down both are dependent on Shift up and Shift down

Build Heap = O(n)

O(n) if we use shift down to build the heap
O(n log(n)) if we use shift up to build the heap

'''

class MinHeap:
	def __init__(self, array):
		# Do not edit the line below.
		self.heap = self.buildHeap(array)

	'''
		Given an unsorted array
		build a minheap - kind of sorted array

		Start from the last element of tree and place every element of that tree in correct position
	'''
	def buildHeap(self, array):
		lastEle = len(array) - 1
		parentIdx = (lastEle - 1) // 2
		print(parentIdx)

		# +1 because i want incluse the current parent as well
		for currentIdx in reversed(range(parentIdx+1)):
			# print(currentIdx)
			self.siftDown(currentIdx,len(array) - 1,array)
		print(array)
		return array
		
	'''
		Compare node to  both of its children node
	'''
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
				childTwoIdx -= 1
				
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
				# if there are no more elements to swap --> just break
				break

	'''
		Continuesly swap the current node with its parent node until the current node is in correct position
	'''
	def siftUp(self,currentIdx,heap):
		# Find the parent element Index
		parentIdx = (currentIdx - 1) // 2
		# check if we are in the indexLimit and not the root element
		# check if the current node is smaller than parent node
		while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
			self.swap(parentIdx, currentIdx,heap)
			currentIdx = parentIdx
			parentIdx = (currentIdx - 1) // 2 # once we reach the root or our elements are heapified then we break out of the loop 

	'''
		The root node will always be the maximum or minimum value in the tree  
	'''
	def peek(self):
		return self.heap[0]


	'''
		Remove the root node - the smallest value or Greatest value   
	'''
	def remove(self):
		self.swap(0,len(self.heap)-1,self.heap)
		valToRemove = self.heap.pop()
		# shift down from the top until last element 
		self.siftDown(0,len(self.heap)-1,self.heap)
		return valToRemove

	'''
		Insert at the end of Tree
		and then move up to its correct position
	'''
	def insert(self, value):
		self.heap.append(value)
		# pass the index of element that needs to shift up and the heap
		# ie the last value we just appended
		self.siftUp(len(self.heap) - 1, self.heap)
		
		
	def swap(self,i,j,heap):
		heap[i] , heap[j] = heap[j] , heap[i]
