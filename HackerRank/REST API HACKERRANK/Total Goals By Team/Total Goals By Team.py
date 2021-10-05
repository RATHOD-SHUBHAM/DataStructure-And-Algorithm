#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#
import requests
def getTotalGoals(team, year):
    # Write your code here
    totalScore = 0
    
    # team 1
    apiCall = requests.get('https://jsonmock.hackerrank.com/api/football_matches?year='+str(year)+'&team1='+str(team)+'&page=1').json()
    
    # print(apiCall)
    
    total_pages = apiCall['total_pages']
    per_page = apiCall['per_page']
    
    for page in range(1,total_pages+1):
        apiCall = requests.get('https://jsonmock.hackerrank.com/api/football_matches?year='+str(year)+'&team1='+str(team)+'&page='+str(page)).json()
        
        try:
            for i in range(0,per_page):
                team1goals = apiCall['data'][i]['team1goals']
                totalScore += int(team1goals)
        except:
            pass
    
    # team 2
    apiCall2 = requests.get('https://jsonmock.hackerrank.com/api/football_matches?year='+str(year)+'&team2='+str(team)+'&page=1').json()
    
    # print(apiCall)
    
    total_pages_2 = apiCall['total_pages']
    per_page_2 = apiCall['per_page']
    
    for page in range(1,total_pages_2+1):
        apiCall2 = requests.get('https://jsonmock.hackerrank.com/api/football_matches?year='+str(year)+'&team2='+str(team)+'&page='+str(page)).json()
        
        try:
            for i in range(0,per_page_2):
                team2goals = apiCall2['data'][i]['team2goals']
                totalScore += int(team2goals)
        except:
            pass
        
    return totalScore
                
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    team = input()

    year = int(input().strip())

    result = getTotalGoals(team, year)

    fptr.write(str(result) + '\n')

    fptr.close()
