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