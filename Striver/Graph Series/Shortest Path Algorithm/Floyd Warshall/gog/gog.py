#User function template for Python
import math

class Solution:
    def floydWarshall(self, dist):
        n = len(dist)

        # Convert -1 to infinity (but keep diagonal as is if it's 0)
        for i in range(n):
            for j in range(n):
                # Ensure diagonal is 0
                if i == j:
                    dist[i][j] = 0
                if dist[i][j] == 10 ** 8:
                    dist[i][j] = math.inf


        # Floyd-Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    cur_dist = dist[i][k] + dist[k][j]
                    dist[i][j] = min(dist[i][j], cur_dist)

        # Check for negative cycles
        for i in range(n):
            if dist[i][i] < 0:
                return 10 ** 8

        # Convert infinity back to -1
        for i in range(n):
            for j in range(n):
                if dist[i][j] == math.inf:
                    dist[i][j] = 10 ** 8

        return dist
                
		                