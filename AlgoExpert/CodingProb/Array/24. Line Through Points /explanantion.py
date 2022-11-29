# Time = O(n^2)
# Space = O(n)

# basic
# horizontal line : slop will be 0 
# if the value are in same straight line then - they will have the same slope



'''

How to save a line?

If the line is horizontal, i.e. y = c, one could use this constant c as a line key in a hash table of horizontal lines.

The other lines could be represented as y = slope * x + c.

The equation for the line passing through two points 1 and 2 could be written through their coordinates as

x - x1     y - y1
------  =  ------
x2 - x1    y2 - y1

that for the representation y = slope * x + c

		rise	y2 - y1
slope = ---- =  -------
		 run	x2 - x1



Since we are drawing a line between the starting point i and each of the following points i+1 ... n, 
if all these lines share the same slope value, 
then we can be sure that all these points are aligned on the same line.

'''

# ----------------------------------------------------------------------


""" 
Dictionary dont allow decimal point as a key.
Our slope might produce a floating number. This can happen when x1 == x2

to avoid the precision issue with the float/double number,
use a pair of co-prime numbers to represent the slope.
"""