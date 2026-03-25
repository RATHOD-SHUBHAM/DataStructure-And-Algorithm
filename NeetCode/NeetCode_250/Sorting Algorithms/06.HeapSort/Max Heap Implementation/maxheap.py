class MaxHeap:

  def __init__(self, arr):
    self.heap = self.buildHeap(arr)

  def buildHeap(self, arr):
    endIdx = len(arr) - 1
    parentIdx = (endIdx - 1) // 2

    for curIdx in reversed(range(parentIdx + 1)):
      self.shiftDown(curIdx, endIdx, arr)
    
    return arr
  
  def shiftDown(self, curIdx, endIdx, heap):
    childOneIdx = (curIdx * 2) + 1

    while childOneIdx <= endIdx:
      childTwoIdx = (curIdx * 2) + 2

      if childTwoIdx > endIdx:
        childTwoIdx = -1

      if childTwoIdx != -1 and heap[childTwoIdx] > heap[childOneIdx]:
        childToSwap = childTwoIdx
      else:
        childToSwap = childOneIdx
      
      if heap[childToSwap] > heap[curIdx]:
        self.swap(heap, childToSwap, curIdx)
        curIdx = childToSwap
        childOneIdx = (curIdx * 2) + 1
      else:
        break
    
  
  def shiftUp(self, curIdx):
    parentIdx = (curIdx - 1) // 2

    while parentIdx >= 0 and self.heap[curIdx] > self.heap[parentIdx]:
      self.swap(self.heap, curIdx, parentIdx)
      curIdx = parentIdx
      parentIdx = (curIdx - 1) // 2
  

  def remove(self):
    firstIdx = 0
    endIdx = len(self.heap) - 1
    self.swap(self.heap, firstIdx, endIdx)

    valTopop = self.heap.pop()

    endIdx = len(self.heap) - 1
    self.shiftDown(firstIdx, endIdx, self.heap)
    return valTopop
  
  def insert(self, val):
    self.heap.append(val)
    endIdx = len(self.heap) - 1
    self.shiftUp(endIdx)
  
  def peek(self):
    return self.heap[0]

  
  def swap(self, arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
  # Test cases
    maxHeap = MaxHeap([ 1, 2, 3, 4, 5 ])
    print("Top Element: ",maxHeap.peek())
    # 5
    maxHeap.insert(12)
    maxHeap.insert(18)
    maxHeap.insert(10)
    print("Top Element: ",maxHeap.peek())
    # 18
    print("Element removed: ",maxHeap.remove())
    print("Top Element: ",maxHeap.peek())
    # 12
    print("Element removed: ",maxHeap.remove())
    print("Top Element: ",maxHeap.peek())
    # 10
    maxHeap.insert(25)
    maxHeap.insert(45)

    print("Element removed: ",maxHeap.remove())
    print("Top Element: ",maxHeap.peek())
    # 25

    print("Element removed: ",maxHeap.remove())
    print("Top Element: ",maxHeap.peek())
    # 10