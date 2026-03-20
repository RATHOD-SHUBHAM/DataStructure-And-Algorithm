class ListNode:

    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        * We are creating a dummy node for each position in the list
        * We use 10 ** 4, because question states at most we will have 10 ** 4 insertions
        """
        self.lst = [ListNode(-1, -1) for _ in range(10**5)]
        

    def put(self, key: int, value: int) -> None:
        # get the position as to where to add -> Hashing will give the position to us
        pos = key % len(self.lst)

        # getting the fist node at that pos -> this will be the dummy node we created
        node = self.lst[pos]

        while node.next:
            if node.next.key == key:
                # update te val if key exist
                node.next.val = value
                return
            
            node = node.next
        
        # We know for sure that the key does not exist in our list -> so we add this at the end
        node.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        # get the position as to where to add -> Hashing will give the position to us
        pos = key % len(self.lst)

        # getting the fist node at that pos -> this will be the dummy node we created
        node = self.lst[pos]

        while node.next:
            if node.next.key == key:
                # returns the value to which the specified key is mapped to.
                return node.next.val
            
            node = node.next
        
        # The map contains no mapping for the key.
        return -1
        

    def remove(self, key: int) -> None:
        # get the position as to where to add -> Hashing will give the position to us
        pos = key % len(self.lst)

        # getting the fist node at that pos -> this will be the dummy node we created
        node = self.lst[pos]

        while node.next:
            if node.next.key == key:
                # removes the key and its corresponding value -> change the pointers
                nxtNode = node.next
                node.next = None
                node.next = nxtNode.next
                nxtNode.next = None

                return
            
            node = node.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)