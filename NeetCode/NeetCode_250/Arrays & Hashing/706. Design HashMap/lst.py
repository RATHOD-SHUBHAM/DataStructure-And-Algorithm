class MyHashMap:

    def __init__(self):
        self.lst = [[-1,-1] for _ in range(10 ** 7)]
        

    def put(self, key: int, value: int) -> None:
        self.lst[key] = value
        

    def get(self, key: int) -> int:
        if self.lst[key][0] == -1:
            # if the key, value pair is not present -> return -1
            return -1
        else:
            # if the key, value pair is present -> return value
            return self.lst[key][1]
        

    def remove(self, key: int) -> None:
        # if the key, value pair is present -> remove it
        if self.lst[key][0] != -1:
            self.lst[key] = [-1,-1]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)