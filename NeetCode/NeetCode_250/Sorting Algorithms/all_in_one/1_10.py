# 1. ================ ================ ================ Bubble Sort ================ ================= =======================

# Tc and Sc: O(n**2)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for _ in range(n):
            for i in range(n-1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            
        return nums

# 2. ================ ================ ================ Selection Sort ================ ================= =======================

# Tc and Sc: O(n^2)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            min_idx = i

            # Find the index of the minimum element in the unsorted part
            for j in range(i, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            
            
            # Swap the found minimum element with the first element of the unsorted part
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        
        return nums


# 2.1 ================ ================ ================ Exchange Sort ================ ================= =======================

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        
        return nums

# 3. ================ ================ ================ Insertion Sort ================ ================= =======================
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Start from the second element, first element alone is trivially sorted
        for i in range(1, n):
            key = nums[i] # Save the element to be inserted
            
            # Compare key with elements to its left, moving backwards
            j = i-1
            while j >= 0 and key < nums[j]:
                # shift every element that is greater than the key one position to the right
                nums[j+1] = nums[j]
                j -= 1
            
            # Place key in its correct position
            nums[j+1] = key

        return nums


# 4. ================ ================ ================ Merge Sort ================ ================= =======================
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)
    
    def mergesort(self, nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2

        # Divide
        left = self.mergesort(nums[ : mid])
        right = self.mergesort(nums[mid : ])

        return self.merge(left, right)
    
    def merge(self, left, right):
        result = []

        i = j = 0

        # Conqure
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            
        # Add the remaining element of the array - which ever is remaining 
        result.extend(left[i : ])
        result.extend(right[j : ])
        
        return result

# 5. ================ ================ ================ Quick Sort ================ ================= =======================
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        startIdx = 0
        endIdx = n - 1
        self.quickSort(nums, startIdx, endIdx)

        return nums

    def quickSort(self, nums, startIdx, endIdx):
        # Check if there is only element in array
        if startIdx >= endIdx:
            return
        
        # Randomly pick pivot and swap it to the start
        randIdx = random.randint(startIdx, endIdx)
        self.swap(nums, startIdx, randIdx)
        
        # Pivot element
        pivot = startIdx
        left = startIdx + 1
        right = endIdx

        # Sort the array so that every element smaller than the pivot goes to its left and every element larger goes to its right. 
        while left <= right:
            if nums[left] > nums[pivot] and nums[right] < nums[pivot]:
                """
                If left ele is greater than pivot and right ele is smaller than pivot -> swap them
                why?
                because every element smaller than the pivot goes to its left and every element larger goes to its right.
                """
                self.swap(nums, left, right)
            
            # Adjust your pointers as per the rule
            if nums[left] <= nums[pivot]:
                left += 1
            
            if nums[right] >= nums[pivot]:
                right -= 1
        
        # place the pivot in its correct final position
        self.swap(nums, pivot, right)

        # Recursively apply quick sort on the left side and right side
        smaller_side = (right - 1) - startIdx <= endIdx - (right + 1)

        if smaller_side:
            self.quickSort(nums, startIdx, right - 1)
            self.quickSort(nums, right+1, endIdx)
        else:
            self.quickSort(nums, right+1, endIdx)
            self.quickSort(nums, startIdx, right - 1)
    

    def swap(self, nums, left, right):
        nums[left], nums[right] = nums[right], nums[left]


# 6. ================ ================ ================ Heap Sort ================ ================= =======================
'''
Formula: 
ChildOne = 2i + 1
ChildTwo = 2i + 2
Parent = (i-1)/2
'''

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

    def printHeap(self):
        for i in range(len(self.heap)):
            print(self.heap[i])


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


# 7. ================ ================ ================ Dutch National Flag Problem ================ ================= =======================


class Solution:
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        ptr = 0
        red = 0 # color 0
        blue = n - 1 # color 2

        while ptr <= blue:
            if nums[ptr] == 2:
                # swap with blue, move blue backward (don't move ptr)
                self.swap(nums, ptr, blue)
                blue -= 1
            
            elif nums[ptr] == 0:
                # swap with red, move both red and ptr forward
                self.swap(nums, ptr, red)
                red += 1
                ptr += 1
            
            else:
                # white's in the right place, just move ptr forward
                ptr += 1

        return nums