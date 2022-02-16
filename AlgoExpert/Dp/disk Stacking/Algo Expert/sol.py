# Time = O(n^2)
# space = O(n)

def diskStacking(disks):
    # sort the disk based on height
	disks.sort(key = lambda x : x[2])
	print(disks)
	
	# keep track of max heights. If current disk is the base
	heights = [disk[2] for disk in disks]
	# print(heights)
	
	# keep track of all the indexes which form max height
	sequence = [None for _ in range(len(disks))]
	# print(sequence)
	
	# keep track of index of max height
	maxHeight_idx = 0
	
	# go through every item in disk and check for tower
	for i in range(1, len(disks)):
		curDisk = disks[i]
		for j in range(0,i):
			prevDisk = disks[j]
			
			# check if smaller condition satisfy
			if curDisk[0] > prevDisk[0] and curDisk[1] > prevDisk[1] and curDisk[2] > prevDisk[2] :
				# check if my cur height is less than combination of previous height
				if heights[i] <= heights[j] + curDisk[2]:
					heights[i] = heights[j] + curDisk[2]
					sequence[i] = j # at cur index add the prev index which is above current disk
					# print(sequence)
	print(heights)
	# print(sequence)
	
	# get index of maximum height
	for i in range(1,len(heights)):
		if heights[i] > heights[maxHeight_idx]:
			maxHeight_idx = i
			
	return getDisks(disks, sequence, maxHeight_idx)

def getDisks(disks, sequence, maxHeight_idx):
	seq = []
	
	while maxHeight_idx is not None:
		seq.append(disks[maxHeight_idx])
		maxHeight_idx = sequence[maxHeight_idx]
	
	# print(seq)
	return list(reversed(seq))
