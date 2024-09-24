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