'''
Given an array of intervals
where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

'''
# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,3],[2,6],[8,10],[9,18]]
intervals = [[1,3],[2,6],[5,10],[9,18]]
# intervals = [[1,4],[4,5]]
result = []

for i in range(len(intervals)-1):
    # print(intervals[i])
    # print(intervals[i][1])
    # print(intervals[i+1])

    if intervals[i][1] >= intervals[i+1][0]:
        print([intervals[i],intervals[i+1]])
        result.append([intervals[i][0],intervals[i+1][1]])

print(result)

'''


# result = [[1,3],[2,6],[8,10],[15,18]]
# print(result[-1][0])

# intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,3],[2,6],[5,10],[9,18]]
intervals = [[1,4],[2,3]]
result = []
intervals.sort()
# print(intervals)

for i in intervals:
    # print(i)
    if result == [] or result[-1][1]<i[0]:
        result.append(i)
    else:
        result[-1][1] = max(result[-1][1],i[1])

print(result)