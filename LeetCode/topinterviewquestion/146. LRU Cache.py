"""
146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
Follow up:
Could you do get and put in O(1) time complexity?




"""

# LRU : if we add item to a stack and the stack is full. It will replace the item with the least recently used item in the stack
# get is nothing but fetch.
# put is nothing but insert
# we will use a hash map and double linked list


# To use double linked list we should first build that. that can be done by creating a class

class Dll:
    #      initializer constructor in python
    # This is creation of the node
    def __init__(self, key, val):
        # node will have a pointer to next and prev node & some value
        # here value is a key,value pair
        self.key = key
        self.val = val
        self.next = None
        self.next = None


class LRUCache:
    #     initialize the cache.
    # here we need a DLL, hashMap, capacity (which is passed by the program itself) and a length to keep track (so that we dont exceed the capacity)
    def __init__(self, capacity: int):
        # this is how to make a initial call to LL
        self.head = Dll(-1, -1)
        self.tail = self.head

        self.hash = {}
        self.capacity = capacity
        self.length = 0

    # DlL will have least recently store element in the front and most recently stored element in the first

    #  return value of the key if exist else return -1
    def get(self, key: int) -> int:
        # ill check if the key exist. if it does ill return the value and the put the node at the end as it was recently visisted to fecth the data.
        if key not in self.hash:
            return -1
        # if the key exist the make the key as the node
        node = self.hash[key]
        # get the value from the node
        val = node.val
        # now that we fetched the value. we have accesed it. So if we acces it we must put it in the end of DLL as it was the most recently accessed node.
        # i need to keep repeating the below steps untli we moce to end. So enclose it in a while loop. Do this until the next node is None
        # for that first step is the remove all the adjucent connection of that particular node
        while node.next:  # do it until there is next node
            node.prev.next = node.next
            node.next.prev = node.prev
            # here we removed all the link

            # now add to the end
            self.tail.next = node
            node.prev = self.tail
            node.next = None

            # now make the last element as tail
            self.tail = node
        return val

    # add the key value to cache. If the stack is full. replacae it with the least recently used item
    def put(self, key: int, value: int) -> None:
        # step 1 :  if key in stack. then jsut put it in the end of DLL becasuse we just now accessed to check if the key exist
        # step 2: else add it to the end of DLL. after adding check if the length of stack doesnot exceed the capacity of the stack. And if it exceeds then pop out the first node from DLL as that is the least recently accessed element.

        # step 1
        if key in self.hash:
            node = self.hash[key]
            val = node.val
            while node.next:  # do it until there is next node
                node.next.prev = node.prev
                node.prev.next = node.next
                # here we removed all the link

                # now add to the end
                self.tail.next = node
                node.prev = self.tail
                node.next = None

                # now make the last element as tail
                node = self.tail
        # step 2
        else:
            # create a new node
            node = Dll(key, value)
            self.hash[key] = node  # adding it to hash map
            # add to it end of Dll
            self.tail.next = node
            node.prev = self.tail
            # make it the last node
            self.tail = node
            # once we add node we goto incremnet length as the length increases
            self.length += 1

            # check if the length increased the capacity of the stack
            if self.length > self.capacity:
                # remove the fist node
                remove = self.head.next
                self.head.next = self.head.next.next
                self.head.next.prev = self.head

                # deleted the first ndoe
                del self.hash[remove.key]
                self.length -= 1  # since we removed a node the length decreases

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)