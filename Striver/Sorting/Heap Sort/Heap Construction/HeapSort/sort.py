# Tc: O(nlog(n)) | Sc: O(1)

class maxHeap:

    def buildHeap(self, array):
        endIdx = len(array) - 1
        parentIdx = (endIdx - 1) // 2

        for curIdx  in reversed(range(parentIdx + 1)):
            self.siftDown(curIdx, endIdx, array)

        return array

    def siftDown(self, curIdx, endIdx, array):
        # Child One Idx = (i * 2) + 1
        childOneIdx = (curIdx * 2) + 1

        while childOneIdx <= endIdx:
            # Child Two Idx = (i * 2) + 2
            childTwoIdx = (curIdx * 2) + 2

            if childTwoIdx > endIdx:
                childTwoIdx = -1

            # Get the largest child
            if childTwoIdx != -1 and array[childTwoIdx] > array[childOneIdx]:
                childToSwap = childTwoIdx
            else:
                childToSwap = childOneIdx

            # Compare and swap with parent idx
            if array[childToSwap] > array[curIdx]:
                self.swap(childToSwap, curIdx, array)
                
                # rearrange pointers
                curIdx = childToSwap

                childOneIdx = (curIdx * 2) + 1
            
            else:
                break

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]

def heapSort(array):
    maxheap = maxHeap()

    maxheap.buildHeap(array)

    # print(array)

    # Now the first element is the greatest element
    for endIdx in reversed(range(1, len(array))):
        swap(0, endIdx, array) # largest element is in its correct place
        # print(array)
        
        maxheap.siftDown(0, endIdx - 1, array) # bring up the next laregst element to the top
        # print(array)

    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]