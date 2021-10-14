'''

A Company performing an analysis on the computers at one of its offices. 
The computers are spaced along a single row. 
The analysis is performed in the following way: 
Choose a contiguous segment of a certain number of computers, 
starting from the beginning of the row.
Analyze the available hard disk space on each of the computers. 
Determine the minimum available disk space within this segment. 
After performing these steps for the first segment, 
it is then repeated for the next segment, 
continuing this procedure until the end of the row 
(i.e. if the segment size is 4, computers 1 to 4 would be analyzed, then 2 to 5, etc.) 
Given this analysis procedure, 
write an algorithm to find the maximum available disk space among all 
the minima that are found during the analysis.



Input
The input consists of three arguments:
numComputer: an integer representing the number of computers
hardDiskSpace: a list of integers representing the hard disk space of the computers
segmentLength: an integer representing the length of the contiguous segment of computers to be considered in each iteration

Output
Return an integer representing 
the maximum available disk space among all the minima that are found during the analysis.


Examples
Input:
numComputer = 3
hardDiskSpace = [62, 64, 77, 75, 71, 60, 79, 75]
segmentLength = 4

Output: 64


'''

from collections import deque
def findMax(hardDiskSpace, k):

    n = len(hardDiskSpace)
    print("n is: ",n)

    print("k is: ",k)

    if n * k == 0:
        return []
    if k > n:
        return []

    deq = deque()
    res = []
    i = 0

    while i < n:

        print("deque: ",deq)
        print("i-k: ",i-k)
        print("\n")
        

        if deq and deq[0] == i - k:
            print("deq[0]: ",deq[0])
            deq.popleft()
            print("deque after pop: ",deq)
            print("\n")

        while deq and hardDiskSpace[deq[-1]] > hardDiskSpace[i]:
            print("hardDiskSpace[deq[-1]]",hardDiskSpace[deq[-1]])
            print("hardDiskSpace[i]",hardDiskSpace[i])
            deq.pop()
            print("deque after pop: ",deq)
            print("\n")

        deq.append(i)
        print("\n")



        print("i: ",i)
        print("k: ",k)
        if i >= k - 1:
            print("hardDiskSpace[deq[0]: ",hardDiskSpace[deq[0]])
            res.append(hardDiskSpace[deq[0]])
        i += 1
    print(res)
    print(max(res))


if __name__ == '__main__':
    hdd = [62, 64, 77, 75, 71, 60, 79, 75]
    k = 4
    findMax(hdd, k)