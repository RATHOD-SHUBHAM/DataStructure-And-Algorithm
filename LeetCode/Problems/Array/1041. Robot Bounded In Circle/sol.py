class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # currently robo is facing north
        curDir = 'N'
        
        # start axis
        x = 0
        y = 0
        
        n = len(instructions)
        
        for i in range(n):
            # current instruction
            cur_ins = instructions[i]
            
            # if its go straight - then x and y axis will change
            if cur_ins == 'G':
                if curDir == 'N':
                    y += 1
                elif curDir == 'S':
                    y -= 1
                elif curDir == 'E':
                    x += 1
                elif curDir == "W":
                    x -= 1
            else:
                # just change in direction
                if curDir == 'N':
                    if cur_ins == 'L':
                        curDir = 'W'
                    else:
                        curDir = "E"
                elif curDir == 'S':
                    if cur_ins == 'L':
                        curDir = 'E'
                    else:
                        curDir = "W"
                elif curDir == 'E':
                    if cur_ins == 'L':
                        curDir = 'N'
                    else:
                        curDir = "S"
                elif curDir == 'W':
                    if cur_ins == 'L':
                        curDir = 'S'
                    else:
                        curDir = "N"
                        
        # In the end if we return back to origin or if our direction is not north then we can circle back to origin
        if (x == 0 and y == 0) or curDir != 'N' : 
            return True
        else:
            return False