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
