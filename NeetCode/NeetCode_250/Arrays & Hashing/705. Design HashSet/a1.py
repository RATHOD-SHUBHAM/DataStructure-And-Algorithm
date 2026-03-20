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

# ---------------------------------------------------------------------------------------------------------

"""
# Optimized: Hashing + Chaining
"""

"""
# Optimized: Hashing + Chaining
"""

class ListNode:

    def __init__(self, key):
        self.val = key
        self.next = None


class MyHashSet:

    def __init__(self):
        """
        * We are creating a dummy node for each position in the list
        * We use 10 ** 4, because question states at most we will have 10 ** 4 insertions
        """
        self.lst = [ListNode(-1) for _ in range(10 ** 4)]
        

    def add(self, key: int) -> None:
        """
        * Add a node at the last postion or last node
        * if there is a node with value, we dont have to re-add as this is a hash set
        """
        # get the position as to where to add -> Hashing will give the position to us
        pos = key % len(self.lst)

        # add the node at that pos
        node = self.lst[pos] # this will give the head node - a dummy start node

        while node.next:
            # check if the key exist while looping
            if node.next.val == key:
                return
            
            node = node.next
        
        node.next = ListNode(key)
        

    def remove(self, key: int) -> None:
        # get the position as to where to add -> Hashing will give the position to us
        pos = key % len(self.lst)

        # Get the head to start iterating
        node = self.lst[pos] # this will give the head node - a dummy start node

        while node.next:
            # check if the key exist while looping
            if node.next.val == key:
                # Change the pointers
                nxtNode = node.next # get the next node
                node.next = None # remove pointer with the node
                node.next = nxtNode.next # attach the next but next node to node
                nxtNode.next = None # detach the next node
                return
            
            # move the pointer
            node = node.next

        

    def contains(self, key: int) -> bool:
        # get the position as to where to add -> Hashing will give the position to us
        pos = key % len(self.lst)

        # Get the head to start iterating
        node = self.lst[pos] # this will give the head node - a dummy start node

        while node.next:
            # check if the key exist while looping
            if node.next.val == key:
                return True
            
            # move the pointer
            node = node.next
        
        # if there is no such node
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)