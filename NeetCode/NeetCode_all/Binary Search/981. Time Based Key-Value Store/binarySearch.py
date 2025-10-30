class TimeMap:

    def __init__(self):
        self.timeStamp = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeStamp[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeStamp:
            return ""
        
        value_list = self.timeStamp[key]

        left = 0
        right = len(value_list) - 1

        res = ""
        while left <= right:
            mid = left + (right - left) // 2

            val = value_list[mid][0]
            ts = value_list[mid][1]

            # continue search to get closer to timestamp
            if ts <= timestamp:
                res = val
                left = mid + 1
            elif ts > timestamp:
                right = mid - 1
        
        return res

            
    
        



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)