# Brute Force: Keep increasing the left element. To give the max element more reward

# always consider my present score to be min and check score to left if there is any score greater
def minRewards(scores):
	reward = [1] * len(scores) # makes sure each get a minimum reward
	
	for i in range(1, len(scores)):
		j = i - 1
		
		# if current score is greater than previous. just add one to prev an make cur score greater
		if scores[i] > scores[j]:
			reward[i] = reward[j] + 1
			
		else:
			# if the current score is less then previous score. Give current score minimum value and increase all the prevous score
			while j >= 0 and scores[j] > scores[j+1]:
				# there might be a condition where array[j] would be greater because of its other adjacent value
				# So check if the current value is more or the one we might get after adding one
				reward[j] = max(reward[j] , reward[j+1] + 1)
				j -= 1
				
	return sum(reward)