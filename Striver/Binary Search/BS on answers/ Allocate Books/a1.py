# ----------------------- Brute Force -----------------------

from typing import List

class Solution:
    def allocate(self, min_pages:int, arr: List[int], m:int, n:int)->int:
        student_count = 1
        pages_assigned = 0

        for i in range(n):
            if pages_assigned + arr[i] <= min_pages:
                pages_assigned += arr[i]
            else:
                pages_assigned = arr[i]
                student_count += 1
        
        return student_count
    
    def allocate_book(self, arr: List[int], m:int, n:int)->int:
        # condition: Each student gets at least one book will not be satisfied.
        if m > n:
            return -1
        
        # How many pages can be assigned to satisfy the conditions
        min_pages = min(arr) # this ensures that everyone can have one book in worst case
        max_pages = sum(arr) # if we assign all pages to one person

        
        # Greedy approach
        for pages in range(min_pages, max_pages + 1):
            student_count =  self.allocate(pages, arr, m, n)

            if student_count == m:
                return pages
        
        return -1

if __name__ == '__main__':
    ob = Solution()

    # Test Case: 1
    arr = [12,34,67,90]
    m = 2
    n = 4

    # Test case: 2
    # arr = [25,46,28,49,94]
    # n = 5
    # m = 4
    result = ob.allocate_book(arr=arr, m=m, n=n)
    print("number of pages assigned to a student is: ", result)


# ----------------------- Binary Search -----------------------


from typing import List

class Solution:
    def allocate(self, min_pages:int, arr: List[int], m:int, n:int)->int:
        student_count = 1
        pages_assigned = 0

        for i in range(n):
            if pages_assigned + arr[i] <= min_pages:
                pages_assigned += arr[i]
            else:
                pages_assigned = arr[i]
                student_count += 1
        
        return student_count
    
    def allocate_book(self, arr: List[int], m:int, n:int)->int:
        # condition: Each student gets at least one book will not be satisfied.
        if m > n:
            return -1
        
        # How many pages can be assigned to satisfy the conditions
        left = min(arr) # this ensures that everyone can have one book in worst case
        right = sum(arr) # if we assign all pages to one person

        min_pages = -1
        
        # Greedy approach
        while left <= right:
            mid = left + (right - left) // 2

            pages = mid
            student_count = self.allocate(pages, arr, m, n)
            
            if student_count <= m:
                right = mid - 1
                min_pages = mid
            else:
                left = mid + 1

        return min_pages


if __name__ == '__main__':
    ob = Solution()

    # Test Case: 1
    # arr = [12,34,67,90]
    # m = 2
    # n = 4

    # Test case: 2
    arr = [25,46,28,49,94]
    n = 5
    m = 4
    result = ob.allocate_book(arr=arr, m=m, n=n)
    print("number of pages assigned to a student is: ", result)