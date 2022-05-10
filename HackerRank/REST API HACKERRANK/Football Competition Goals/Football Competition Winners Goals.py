#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getWinnerTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING competition
#  2. INTEGER year
#
import requests

def params(team,year,page,whichTeam,competition):
    print({
        'year':str(year),
        'team'+str(whichTeam): team,
        'page':page,
        'competition':competition
    })
    return{
        'year':str(year),
        'team'+str(whichTeam): team,
        'page':page,
        'competition':competition
}

def handleRequest(team,year,page,whichTeam=1,competition=''):
    URL = 'https://jsonmock.hackerrank.com/api/football_matches'
    req = requests.get(url = URL, params= params(team,year,page,whichTeam,competition))
    
    data = req.json()
    print(data)
    
    return data

def handleData(team, whichTeam, competition):
    teamNum = 'team' + str(whichTeam) + 'goals'
    print(teamNum)
    goals = 0
    
    collection_of_match = handleRequest(team,year,1,whichTeam,competition)
    
    totalPages = collection_of_match['total_pages']
    perPage = collection_of_match['per_page']
    
    for i in range(1,totalPages+1):
        apiCall = handleRequest(team,year,i,whichTeam,competition)
        print('apiCall for page {0} data is {1}'.format(i,apiCall))
        
        try:
            for j in range(0,perPage):
                goals+=int(apiCall['data'][j][teamNum])
        except:
            pass
        
        print(goals)
                
    
    return goals


def getTotalGoals(team,year,competition):
    totalGoal = 0
    # first request to get the pagination details
    totalGoal += handleData(team, 1, competition)
    totalGoal += handleData(team, 2, competition)
    
    return totalGoal

# get the winner name
def getWinnerTotalGoals(competition, year):
    # Write your code here
    URL = 'https://jsonmock.hackerrank.com/api/football_competitions'
    params = {
        'name' : competition,
        'year' : str(year)
    }
    
    apiCall = requests.get(URL,params).json()
    print(apiCall)
    
    team = apiCall['data'][0]['winner']
    print(team)
    return getTotalGoals(team,year,competition)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    competition = input()

    year = int(input().strip())

    result = getWinnerTotalGoals(competition, year)

    fptr.write(str(result) + '\n')

    fptr.close()