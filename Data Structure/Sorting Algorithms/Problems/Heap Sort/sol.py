def heapSort(array):
    # Write your code here.
	lastEle = len(array) - 1
	buildHeap(array,lastEle)
	
	for endIdx in reversed(range(1,len(array))):
		swap(0,endIdx,array)
		shiftDown(0,endIdx-1,array)
	
	return array

def buildHeap(array,lastEle):
	parentIdx = (lastEle - 1) // 2
	
	for i in reversed(range(parentIdx + 1)):
		shiftDown(i,lastEle,array)
		
	return array

def shiftDown(currentIdx,endIdx,array):
	childOne = (2 * currentIdx) + 1
	# endIdx = len(array) - 1
	
	while childOne <= endIdx:
		if ((2 * currentIdx) + 2) <= endIdx:
			childTwo = (2 * currentIdx) + 2
		else:
			childTwo = -1
			
		if childTwo != -1 and array[childTwo] > array[childOne]:
			childToSwap = childTwo
		else:
			childToSwap = childOne
			
		if array[childToSwap] > array[currentIdx]:
			swap(childToSwap,currentIdx,array)
			currentIdx = childToSwap
			childOne = (2 * currentIdx) + 1
		else:
			return
	

def swap(l,r,array):
	array[l], array[r] = array[r], array[l]