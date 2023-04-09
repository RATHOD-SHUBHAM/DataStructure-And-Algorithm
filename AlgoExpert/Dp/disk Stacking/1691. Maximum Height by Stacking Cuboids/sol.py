class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        n = len(cuboids)
        
        # Sort so that max value becomes height
        for cube in cuboids:
            cube.sort()
        
        # Sort so that max width will become bottom
        
        cuboids.sort()
        # print(cuboids)
        
        height = [x[2] for x in cuboids]
        # print(height)
        
        for i in range(1, n):
            curCube = cuboids[i]
            
            for j in range(0 , i):
                prevCube = cuboids[j]
                
                if prevCube[0] <= curCube[0] and prevCube[1] <= curCube[1] and prevCube[2] <= curCube[2]:
                    
                    if height[i] <= height[j] + curCube[2]:
                        height[i] = height[j] + curCube[2]
                        
        # print(height)
        return max(height)