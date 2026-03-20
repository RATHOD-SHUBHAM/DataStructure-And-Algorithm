"""
# Brute Force : Using List
"""
class MyHashSet:

    def __init__(self):
        self.lst = [-1] * 10 ** 7
        

    def add(self, key: int) -> None:
        self.lst[key] = key
        

    def remove(self, key: int) -> None:
        self.lst[key] = -1
        

    def contains(self, key: int) -> bool:
        if self.lst[key] != -1:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)