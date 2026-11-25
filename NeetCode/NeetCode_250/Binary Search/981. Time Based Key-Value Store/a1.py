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

# ============================================ 981. Time Based Key-Value Store ============================================
class TimeMap:
    def __init__(self):
        self.store = {}                      # key -> (timestamps, values)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            # if key is not there, then create empty list to insert the key {val, timestamp} in the dic
            self.store[key] = ([], [])     # dict now holds: key -> (empty times list, empty vals list)
        
        # grab the list if already existing
        times, vals = self.store[key]      # times and vals point at THOSE SAME lists
        times.append(timestamp)            # changes the list inside the dict
        vals.append(value)                 # changes the list inside the dict

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        
        times, vals = self.store[key]

        left = 0 
        right = len(times)

        while left < right:
            mid = (left + right) // 2

            if times[mid] <= timestamp:
                left = mid + 1               # mid is allowed, look right
            else:
                right = mid                  # mid is too new, keep as boundary
        
        # left = first index with time > timestamp
        return vals[left - 1] if left > 0 else ""
