def hasSingleCycle(array):
    pass

if __name__ == "__main__":
    array = [2, 3, 1, -4, -4, 2]
    print(hasSingleCycle(array))

    # Test case 2: Not a single cycle
    array2 = [1, 1, -1, -1]
    print(hasSingleCycle(array2))

    # Test case 3: Single element pointing to itself
    array3 = [1]
    print(hasSingleCycle(array3))

    # Test case 4: Early return to start
    array4 = [3, 1, 1, 1]
    print(hasSingleCycle(array4))