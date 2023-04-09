# Tc: O(n^2) | Sc: O(n)
def diskStacking(disks):
    # Write your code here.
    n = len(disks)

    # Sort so that max width will become bottom
    disks.sort() 
    # print(disks)

    # keep track of all the stack up until that index
    height = [x[2] for x in disks]

    # keep track of sequence to build the stack
    sequence = [None] * n

    # we try building stack by making curDisk as the base and keep adding prevDisk on top of it
    for i in range(1 , n):
        curDisk = disks[i]

        for j in range(0,i):
            prevDisk = disks[j]

            # disk must be strictly smaller than below disk
            if prevDisk[0] < curDisk[0] and prevDisk[1] < curDisk[1] and prevDisk[2] < curDisk[2]:
                # check if the prevDisk has a stack of itself
                if height[i] < height[j] + curDisk[2]:
                    height[i] = height[j] + curDisk[2]
                    sequence[i] = j

    # print(height)
    # print(sequence)

    # get the index of max height
    max_height = height[0]
    index = 0

    for i in range(1, n):
        if height[i] > max_height:
            max_height = height[i]
            index = i

    # print(index)

    return buildStack(index, sequence, disks)

def buildStack(index, sequence, disks):
    stack_sequence = []

    while index is not None:
        stack_sequence.append(disks[index])
        index = sequence[index]

    # print(stack_sequence)
    return stack_sequence[::-1]
