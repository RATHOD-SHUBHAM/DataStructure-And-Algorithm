import heapq

def laptopRentals(times):
    # Write your code here.
    if len(times) == 0:
        return 0

    times.sort(key = lambda x : x[0])

    min_no_of_laptop = [times[0][1]]

    heapq.heapify(min_no_of_laptop)

    for i in range(1, len(times)):
        curInterval = times[i]

        if min_no_of_laptop[0] <= curInterval[0]:
            heapq.heappop(min_no_of_laptop)

        heapq.heappush(min_no_of_laptop , curInterval[1])

    return len(min_no_of_laptop)
    
