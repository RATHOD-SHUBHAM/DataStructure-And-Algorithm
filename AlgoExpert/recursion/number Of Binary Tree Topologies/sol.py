'''
when n = 3
3-1 # root node
if there is one node on left then there can be only one on right
		o          or if there are 2 node on left there will be none 
	   / \             o
	  o   o           /
					 o
					/
				   o
'''
# Time = O(n^2)
# Space = O(n)


def numberOfBinaryTreeTopologies(n):
    if n == 0:
        return 1
	
    result = 0
    for leftTreeSize in range(n):
        
        rightTreeSize = n - 1 - leftTreeSize # if there are no left tree then nodes are present in right tree
        no_of_left_tree = numberOfBinaryTreeTopologies(leftTreeSize)
        no_of_right_tree = numberOfBinaryTreeTopologies(rightTreeSize)
        
        result += no_of_left_tree * no_of_right_tree
        
        print("left : ",leftTreeSize)
        print("right : ",rightTreeSize)
        print("result : ", result)
            
    return result