# typical logical operator example
'''
False or False = Flase

Rest everything is True
'''
def isMonotonic(array):
    increasing = True
	decresing = True
	
	for i in range(1,len(array)):
		if array[i] > array[i-1]:
			decresing = False
		if array[i] < array[i-1]:
			increasing = False
			
	return increasing or decreasing 

'''
	if any where in between suddenly the value change
	then one of the flag become true

	But thats fine. one flag can be false and one can be true


	but if both the flag turns false

	then that means the value inc or dec (vise versa)

'''

