class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    '''
        Create heap of array
    '''
    def buildHeap(self, array):
        endIdx = len(array) - 1
        
        # Parent idx = (i - 1) // 2
        parentIdx = (endIdx - 1) // 2

        # Build heap for current tree
        for currentIdx in reversed(range(parentIdx + 1)):
            self.siftDown(currentIdx, endIdx, array)

        return array

    '''
        Move the current node to its correct position by travelling downward
    '''
    def siftDown(self, curIdx, endIdx, array):
        # Child One Idx = (i * 2) + 1
        childOneIdx = (curIdx * 2) + 1

        while childOneIdx <= endIdx:
            # Child Two Idx = (i * 2) + 2
            childTwoIdx = (curIdx * 2) + 2

            if childTwoIdx > endIdx:
                childTwoIdx = -1

            # Get the smallest child
            if childTwoIdx != -1 and array[childTwoIdx] < array[childOneIdx]:
                childToSwap = childTwoIdx
            else:
                childToSwap = childOneIdx

            # Compare and swap with parent idx
            if array[childToSwap] < array[curIdx]:
                self.swap(childToSwap, curIdx, array)
                
                # rearrange pointers
                curIdx = childToSwap

                childOneIdx = (curIdx * 2) + 1
            
            else:
                break
                

    '''
        Move the current node to its correct position by travelling upward
    '''
    def siftUp(self, curIdx, array):
        
        parentIdx = (curIdx - 1) // 2

        while curIdx > 0 and array[curIdx] < array[parentIdx]:
            self.swap(curIdx, parentIdx, array)

            # Rearrange pointers
            curIdx = parentIdx

            parentIdx = (curIdx - 1) // 2

            

    '''
        Top of tree is the min/max number
    '''
    def peek(self):
        return self.heap[0]

    '''
        Remove the head by swapping it to end
        then placed the swapped node in its correct position by moving it down
    '''
    def remove(self):
        endIdx = len(self.heap) - 1
        
        # Bring the head to end 
        self.swap(0, endIdx, self.heap)

        valToremove = self.heap.pop()

        self.siftDown(0, endIdx, self.heap)

        return valToremove

    '''
        Insert at the end and then move up to correct position
    '''
    def insert(self, value):
        self.heap.append(value)

        endIdx = len(self.heap) - 1
        
        self.siftUp(endIdx, self.heap)

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]
