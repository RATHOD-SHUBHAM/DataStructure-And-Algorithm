class Solution:
    def getLucky(self, s: str, k: int) -> int:
        n = len(s)

        transform = ""

        for i in range(n):
            transform += str((ord(s[i]) - ord('a')) + 1)
        
        # print(transform)

        while k > 0:
            count = 0
            for i in transform:
                count += int(i)
                # print(count)

            transform = str(count)
            k -= 1
        
        return int(transform)
            