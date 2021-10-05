def tournamentWinner(competitions, results):
	bestTeam = '' # keep track of the winning team
	scoreBoard = {bestTeam : 0}
	
	for idx,team in enumerate(competitions):
		result = results[idx]

        # destructuring
		homeTeam, awayTeam = team
		
		winningTeam = homeTeam if result == 1 else awayTeam
		
		if winningTeam not in scoreBoard:
			scoreBoard[winningTeam] = 0
			
		scoreBoard[winningTeam] += 3
		
		if scoreBoard[winningTeam] > scoreBoard[bestTeam]:
			bestTeam = winningTeam
			
	return bestTeam
	