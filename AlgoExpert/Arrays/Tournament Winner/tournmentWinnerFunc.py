def updateScoreBoard(winningTeam,scoreBoard):
	if winningTeam not in scoreBoard:
		scoreBoard[winningTeam] = 0
		
	scoreBoard[winningTeam] += 3

def tournamentWinner(competitions, results):
    bestTeam = ''
	scoreBoard = {bestTeam : 0}
	
	for idx,team in enumerate(competitions):
		result = results[idx]
		homeTeam,awayTeam = team
		
		winningTeam = homeTeam if result == 1 else awayTeam
		
		updateScoreBoard(winningTeam,scoreBoard)
		
		if scoreBoard[winningTeam] > scoreBoard[bestTeam]:
			bestTeam = winningTeam
			
	return bestTeam
