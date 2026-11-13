# ================================= In RANGE CYCLE SORT =====================================

# Range will work for only positive number as range is between [1 ... N]
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

# ================================= NON RANGE CYCLE SORT =====================================

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