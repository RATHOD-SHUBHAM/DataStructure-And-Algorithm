'''

Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer a

Guaranteed constraints:
1 ≤ a.length ≤ 100,
a[i].length = a.length,
1 ≤ a[i][j] ≤ 104.

[output] array.array.integer




'''



'''

LOGIC IS TO FIRST TRANSPOSE THE MATRIX AND REVERSE IT => INORDER FOR THE MATRIX TO ROTATE BY 90 DEGREE

'''

# Time = O(n^2)
# Space = O(1)

def rotateImage(a):
    n = len(a[0]) # get the length of matrix

    # transpose the matrix
    for i in range(n):
        for j in range(i):
            '''
            a[i][j] = a[j][i]
            a[j][i] = a[i][j]
            
            '''
            a[i][j],a[j][i] = a[j][i], a[i][j]

    # reverse the transpose matrix:

    for i in range(n):
        a[i].reverse()

    return a
            