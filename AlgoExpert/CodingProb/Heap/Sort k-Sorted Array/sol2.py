import heapq

def sortKSortedArray(array, k):
    # Write your code here.
    minHeap = array[ : min( k + 1 , len(array))]
    heapq.heapify(minHeap)

    idxToappend = 0

    for idx in range(k+1 , len(array)):
        # print(minHeap)
        valToappend = heapq.heappop(minHeap)
        array[idxToappend] = valToappend
        idxToappend += 1

        heapq.heappush(minHeap , array[idx])
        

    while len(minHeap) > 0:
        # print(minHeap)
        valToappend = heapq.heappop(minHeap)
        array[idxToappend] = valToappend
        idxToappend += 1

    return array
