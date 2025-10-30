class TimeMap:

    def __init__(self):
        self.timeStamp = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeStamp[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeStamp:
            return ""
        
        value_list = self.timeStamp[key]

        for i in reversed(range(len(value_list))):
            val , ts = value_list[i]

            if ts <= timestamp:
                return val

        return ""
        



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)