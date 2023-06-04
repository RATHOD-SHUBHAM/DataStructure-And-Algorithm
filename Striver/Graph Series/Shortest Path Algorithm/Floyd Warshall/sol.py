#User function template for Python

import math

class Solution:
	def shortest_distance(self, matrix):
        
        n = len(matrix)

        # since i will cal min distance. Lets change the -1 to inf
        # also lets fill the diagonals with 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    matrix[i][j] = 0
                if matrix[i][j] == -1:
                    matrix[i][j] = math.inf


        # multi source shortest path
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    cur_cost = matrix[i][k] + matrix[k][j]
                    matrix[i][j] = min(matrix[i][j], cur_cost)

        # check for negative cycle
        for i in range(n):
            if martrix[i][i] < 0:
                return -1

        # if any cell if unrechable we need to return -1
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == math.inf:
                    matrix[i][j] = -1


        return matrix