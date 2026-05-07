class CycleSort:
    def sort(self, arr):
        n = len(arr)

        # Loop through all the element
        for cycle_start in range(0, n-1):
            
            item = arr[cycle_start] # get item at current index

            # Place this item at its correct position
            pos = cycle_start

            # Step 1: Find all the elements smaller than current element
            for i in range(cycle_start + 1, n):
                if arr[i] < item:
                    pos += 1
            
            # Check if the item is already in its correct position
            if pos == cycle_start:
                continue

            # Skip duplicates
            while item == arr[pos]:
                pos += 1
            
            # Place the item at its correct position
            if item != arr[pos]:
                    item, arr[pos] = arr[pos], item

            # Step 2: Place the other displaced elements in its correct position
            while pos != cycle_start:
                pos = cycle_start

                # Find all the elements smaller than current element
                for i in range(cycle_start + 1, n):
                    if arr[i] < item:
                        pos += 1

                # Skip duplicates
                while item == arr[pos]:
                    pos += 1
                
                # Critical: Place the item at its correct position
                if item != arr[pos]:
                    item, arr[pos] = arr[pos], item
        
        return arr
    

if __name__ == "__main__":
    ob = CycleSort()

    # Basic Test 

    arr = [3,5,2,1,4]
    op_arr = ob.sort(arr=arr)
    print(op_arr)

    arr = [3, 1, 2]
    op_arr = ob.sort(arr=arr)
    print(op_arr)

    arr = [2, 1, 4, 3]
    op_arr = ob.sort(arr=arr)
    print(op_arr)

    # Already Sorted

    arr = [1, 2, 3, 4]
    op_arr = ob.sort(arr=arr)
    print(op_arr)

    arr = [1]
    op_arr = ob.sort(arr=arr)
    print(op_arr)

    # Reverse Sorted

    arr = [4, 3, 2, 1]
    op_arr = ob.sort(arr=arr)
    print(op_arr)

    arr = [5, 4, 3, 2, 1]
    op_arr = ob.sort(arr=arr)
    print(op_arr)

    
    # Duplicates
    arr = [2,2,1]
    op_arr = ob.sort(arr=arr)
    print(op_arr)

    arr = [1, 1, 2]
    op_arr = ob.sort(arr=arr)
    print(op_arr)

    arr = [3, 2, 2, 1]
    op_arr = ob.sort(arr=arr)
    print(op_arr)

    arr = [2, 1, 2, 3]
    op_arr = ob.sort(arr=arr)
    print(op_arr)

    # All Same
    arr = [2, 2, 2, 2]
    op_arr = ob.sort(arr=arr)
    print(op_arr)

    arr = [1, 1, 1, 1]
    op_arr = ob.sort(arr=arr)
    print(op_arr)

    # Two Elements
    arr = [2, 1]
    op_arr = ob.sort(arr=arr)
    print(op_arr)

    arr = [1, 2]
    op_arr = ob.sort(arr=arr)
    print(op_arr)

    # Negatives
    arr = [3, -1, 2, 1, -5]
    op_arr = ob.sort(arr=arr)
    print(op_arr)

    arr = [-3, -1, -2, -5]
    op_arr = ob.sort(arr=arr)
    print(op_arr)
