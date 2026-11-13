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
