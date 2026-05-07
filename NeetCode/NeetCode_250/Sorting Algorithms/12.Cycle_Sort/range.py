class CycleSort:
    def sort(self, arr):
        n = len(arr)

        i = 0

        while i < n:

            correct_idx = arr[i] - 1

            # Place the element at its correct index
            if arr[i] != arr[correct_idx]:
                arr[i], arr[correct_idx] = arr[correct_idx], arr[i]

            else:
                i += 1

        return arr    

if __name__ == "__main__":
    # Range will work for only positive number as range is between [1 ... N]
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
