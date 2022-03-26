# Problem is a great way to work on enumeration problem
def tournamentWinner(competitions, results):
    currentBest_Team = ""
	score_board = {currentBest_Team : 0}
	
	# now keep track of the best team
	for idx, teams in enumerate(competitions):
		# get the result for that competition
		result = results[idx]
		
		# extra value from comprehended list
		home_team , away_team = teams
		
		# get the winning team and increase its points on score board by 3
		winning_team = home_team if result == 1 else away_team
		
		if winning_team not in score_board:
			score_board[winning_team] = 0
		
		score_board[winning_team] += 3
		
		
		# keep track of the best team
		if score_board[winning_team] > score_board[currentBest_Team]:
			currentBest_Team = winning_team
			
	return currentBest_Team