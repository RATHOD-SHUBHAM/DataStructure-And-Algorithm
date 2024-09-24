# ------------------------------------- Brute Force -------------------------------------

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        sorted_number = []

        # Check for every combination form 1 - 9
        for i in range(1, 10):
            self.getNextNumber(n, sorted_number, cur_num = i)
        
        return sorted_number
    
    def getNextNumber(self, n, sorted_number, cur_num):
        if cur_num > n:
            return
        
        sorted_number.append(cur_num)
        
        for next_num in range(10):
            # Add a new digit to the end
            new_num = cur_num * 10 + next_num

            if new_num <= n:
                self.getNextNumber(n, sorted_number, cur_num = new_num)
            else:
                break
        
        return
    

# ------------------------------------- Optimal Solution -------------------------------------

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        sorted_number = []

        cur_num = 1

        for _ in range(n):
            sorted_number.append(cur_num)

            if cur_num * 10 <= n:
                cur_num = cur_num * 10
            else:
                # if the number is 19,29,39 etc or cur_num > n, extract the Left number
                while cur_num % 10 == 9 or cur_num >= n:
                    cur_num = cur_num // 10
                
                # increment the number
                cur_num += 1
        
        return sorted_number
