def spiralTraverse(array):
	result = []
	
	'''Start row, Start Col , End row, End Col'''
	sr = 0
	sc = 0
    
	er = len(array) - 1
	ec = len(array[0]) - 1
	
	while sr <= er and sc <= ec:
		for col in range(sc,ec+1):
			result.append(array[sr][col])
		print(result)
			
		for row in range(sr+1, er+1):
			result.append(array[row][ec])
		print(result)
			
		for col in reversed(range(sc,ec)):
			if sr == er:
				break
			result.append(array[er][col])
		print(result)
			
		for row in reversed(range(sr+1,er)):
			if sc == ec:
				break
			result.append(array[row][sc])
		print(result)
			
		sr += 1
		sc += 1
		er -= 1
		ec -= 1
		
	return result