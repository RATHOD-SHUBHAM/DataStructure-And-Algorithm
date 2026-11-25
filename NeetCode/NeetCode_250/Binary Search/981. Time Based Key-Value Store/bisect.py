class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = ([], [])

        val, tme = self.dict[key]
        val.append(value)
        tme.append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        
        val, tme = self.dict[key]

        idx = bisect.bisect_right(tme, timestamp)
        # if we do bisect left then there is a hidden issue that comes up of how do we return
        # bisect left = nums[i] >= t
        # so if we found the target we return i,
        # if target is not there, ie nums[i] > t, then we have to return i - 1
        # but how do we understand when to return i or i-1
        # but with bisect right , we can always return i - 1

        return val[idx - 1] if idx - 1 >= 0 else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)