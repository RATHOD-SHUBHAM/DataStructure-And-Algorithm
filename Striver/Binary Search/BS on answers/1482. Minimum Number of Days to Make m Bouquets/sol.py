class Solution:    
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)

        if n < m * k:
            return -1

        minDay = -1

        left = min(bloomDay)
        right = max(bloomDay)

        while left <= right:
            mid = left + (right - left) // 2

            no_of_bouquet = 0
            count = 0
            for bloom_day in bloomDay:
                if bloom_day <= mid:
                    count += 1
                else:
                    count = 0
                
                if count == k:
                    no_of_bouquet += 1
                    count = 0
            
            if no_of_bouquet < m:
                left = mid + 1
            else:
                # You can make m or more bouquets
                minDay = mid
                right = mid - 1
        
        return minDay


# -------------- Same Solution : Extracting Layer --------------

class Solution:
    def checkBouquetPossible(self, mid, k, bloomDay):
        no_of_bouquet = 0
        count = 0

        for bloom_day in bloomDay:
            if bloom_day <= mid:
                count += 1
            else:
                count = 0
            
            if count == k:
                no_of_bouquet += 1
                count = 0
        
        return no_of_bouquet
    
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)

        if n < m * k:
            return -1

        minDay = -1

        left = min(bloomDay)
        right = max(bloomDay)

        while left <= right:
            mid = left + (right - left) // 2

            no_of_bouquet = self.checkBouquetPossible(mid, k, bloomDay)
            
            if no_of_bouquet < m:
                left = mid + 1
            else:
                # You can make m or more bouquets
                minDay = mid
                right = mid - 1
        
        return minDay
        
