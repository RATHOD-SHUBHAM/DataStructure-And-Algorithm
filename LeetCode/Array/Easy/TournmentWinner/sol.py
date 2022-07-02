# Time Complexity: O(n) , N is the number of competitions
# Space Complexity: O(n) , N is the no of teams

def tournamentWinner(competitions, results):
    currentBest = ""
	# because first time we compare with a string we need to add it to dictionary
	scores = {currentBest : 0}
	
	for idx , comp in enumerate(competitions):
		result = results[idx]
		
		homeTeam, awayTeam = comp
		
		winningTeam = homeTeam if result == 1 else awayTeam
		
		updateScores(winningTeam, scores)
		
		if scores[winningTeam] > scores[currentBest]:
			currentBest = winningTeam
			
	return currentBest

def updateScores(winningTeam, scores):
	if winningTeam not in scores:
		scores[winningTeam] = 0
		
	scores[winningTeam] += 3