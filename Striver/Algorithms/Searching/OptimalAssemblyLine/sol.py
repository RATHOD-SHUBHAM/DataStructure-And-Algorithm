'''
    Goal is to figure out what is the optimal configuration such that, whatever station is going to take the longest time step, can have lowest duration possible 

Steps:
    1. Get the optimal time.
    2. Check if this is the optimal time.
'''

import math

def optimalAssemblyLine(stepDurations, numStations):
    # single station with one assembly can have a max time of
    left = max(stepDurations)

    # single station can have all the station in it
    right = sum(stepDurations)

    # longest duration in a station line after optimizing the assembly line
    # we cannot have assembly line lesser than this
    longest_optimal_duration = math.inf


    while left <= right:
        # Lets assume mid is the optimal duration each station can hold, now lets check if this will yield optimal solution
        mid = left + (right - left) // 2
        
        if isOptimized(mid, stepDurations, numStations):
            '''
                If this can hold the current duration, try reducing the duration to check if there is more optimal solution
            '''
            
            longest_optimal_duration = mid
            right = mid - 1

        else:
            left = mid + 1

    return longest_optimal_duration

def isOptimized(current_optimal_duration, stepDurations, numStations):
    stationCount = 1
    currentDuration = 0

    for stepDuration in stepDurations:
        if currentDuration + stepDuration > current_optimal_duration:
            stationCount += 1
            currentDuration = stepDuration
        else:
            currentDuration += stepDuration

    if stationCount <= numStations:
        '''
            If the number of station available is able to accomodate all the assemly line in the given time time, then return true
        '''
        return True
    else:
        return False