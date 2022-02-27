# Time and Space = O(c1 + c2)

def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
	# step 1:
	# update calender. basically before their work start time . we can say that they are busy and not available for meeting
	updatedCalendar1 = updateCalendar(calendar1, dailyBounds1)
	# print(updatedCalendar1)
	updatedCalendar2 = updateCalendar(calendar2, dailyBounds2)
	# print(updatedCalendar2)

	# step 2:
	# merge the calendar into a single one. Easy for comparision
	mergedCalendar = mergeCalendar(updatedCalendar1 ,  updatedCalendar2)
	# print(mergedCalendar)
	
	# step 3:
	# flatten the calendar: Merge the meeting that are overlapping
	flatCalendar = flattenedCalendar(mergedCalendar)
	print(flatCalendar)
	
	
	# step 4:
	# return the available spots
	return getAvailableSpot(flatCalendar , meetingDuration)

def updateCalendar(calendar, dailyBounds):
	updatedCalendar = calendar[:]
	
	# insert at index 0, early morning to office start time
	updatedCalendar.insert(0, ["0:00",dailyBounds[0]])
	
	# append in the end. office end time and end time of day
	updatedCalendar.append([dailyBounds[1], "23:59"])
	
	return list(map(lambda x: [hoursToMin(x[0]), hoursToMin(x[1])],updatedCalendar))


def hoursToMin(time):
	hours, minutes = list(map(int, time.split(":")))
	# print(hours, minutes)
	return hours * 60 + minutes



def mergeCalendar(calendar1 ,  calendar2):
	mergedCalendar = []
	
	# perform merge sort, and merge on basis of start time
	i = j = 0
	
	while i < len(calendar1) and j < len(calendar2):
		meeting1 = calendar1[i]
		meeting2 = calendar2[j]
		
		if meeting1[0] < meeting2[0]:
			mergedCalendar.append(meeting1)
			i += 1
		else:
			mergedCalendar.append(meeting2)
			j += 1
		
	while i < len(calendar1):
		mergedCalendar.append(meeting1)
		i += 1
	
	while j < len(calendar2):
		mergedCalendar.append(meeting2)
		j += 1
		
	return mergedCalendar

def flattenedCalendar(mergedCalendar):
	calendar = mergedCalendar[:]
	flatCalendar = [calendar[0]]

	for i in range(1, len(calendar)):
		# print(calendar[i])
		curMeeting_start = calendar[i][0]
		curMeeting_end = calendar[i][1]
		
		# print(flatCalendar[-1])
		prevMeeting_start = flatCalendar[-1][0]
		prevMeeting_end = flatCalendar[-1][1]
		
		
		# if the meeting are overlapping. Merge them
		if curMeeting_start <= prevMeeting_end:
			# since the calendar is sorted prev meeting start will be earliest time
			newMeeting_time = [prevMeeting_start, max(curMeeting_end, prevMeeting_end)]
			# print(newMeeting_time)
			# print("\n")
			# replace the previous meeting with new time
			flatCalendar[-1] = newMeeting_time
		else:
			flatCalendar.append(calendar[i])
		
	return flatCalendar


def getAvailableSpot(flatCalendar , meetingDuration):
	availableSpot = []
	
	for i in range(1,len(flatCalendar)):
		prevMeeting_EndTime = flatCalendar[i-1][1]
		curMeeting_StartTime = flatCalendar[i][0]
		
		if curMeeting_StartTime - prevMeeting_EndTime >= meetingDuration:
			availableSpot.append([prevMeeting_EndTime , curMeeting_StartTime ])
			
	print(availableSpot)
	return list(map(lambda x : [minToHour(x[0]) , minToHour(x[1])],availableSpot))
		

def minToHour(time):
	hours = time // 60
	minutes = time % 60
	
	hoursString = str(hours)
	
	if minutes > 9:
		minutesToString = str(minutes)
	else:
		minutesToString = "0" + str(minutes)
		
	return hoursString + ":" + minutesToString
		