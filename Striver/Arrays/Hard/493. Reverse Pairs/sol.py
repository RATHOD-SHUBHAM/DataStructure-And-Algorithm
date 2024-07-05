class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        return self.mergeSort(left, right, nums)
    
    def mergeSort(self, left, right, nums):
        if right - left < 1:
            return 0
        
        mid = left + (right - left) // 2


        # Divide the array
        leftArray = self.mergeSort(left, mid, nums)
        rightArray = self.mergeSort(mid + 1, right, nums)

        # Count number of inversion
        count_pair = self.countInversion(left, mid + 1, right, nums)

        reverse_pair_count = leftArray + rightArray + count_pair

        # Merge the array
        self.merge(left, mid + 1, right, nums)

        return reverse_pair_count
    
    def countInversion(self, left, start, right, nums):
        '''
            left : start of left array

            start: start of right array
            right: end of right array
        '''
        reverse_pair_count = 0

        j = start

        for i in range(left, start):
            while j <= right and nums[i] > 2 * nums[j]:
                j += 1
            
            reverse_pair_count += j - start
        
        return reverse_pair_count
    
    def merge(self, left, start, right, nums):
        '''
            left : start of left array

            start: start of right array
            right: end of right array
        '''
        sorted_array = []

        i = left
        j = start

        while i < start and j < right + 1:
            if nums[i] <= nums[j]:
                sorted_array.append(nums[i])
                i += 1
            else:
                sorted_array.append(nums[j])
                j += 1

        
        sorted_array += nums[i : start] + nums[j : right + 1]

        # Add it back to main array
        for i in range(len(sorted_array)):
            nums[left + i] = sorted_array[i]
        
        return