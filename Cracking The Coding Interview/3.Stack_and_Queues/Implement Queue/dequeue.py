# deque

from collections import deque

class deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # using append() to insert element at right end 
    def enqueue(self, item):
        self.items.append(item)

    # using appendleft() to insert element at left end 
    def enqueue_front(self, item):
        self.items.appendleft(item)

    # using extend() to add numbers to right end 
    def extend(self, items):
        self.items.extend(items)
    
    # using extendleft() to add numbers to left end 
    def extendleft(self, items):
        self.items.extendleft(items)

    # using insert() to insert the value eg:3 at eg:5th position
    def insert(self, index, item):
        self.items.insert(index, item)

    # using pop() to delete element from right end 
    def dequeue(self):
        return self.items.pop()

    # using popleft() to delete element from left end 
    def dequeue_front(self):
        return self.items.popleft()

    # using remove() to remove the first occurrence of number from deque
    def remove(self, item):
        self.items.remove(item)

    def size(self):
        return len(self.items)

    # using index() to print the first occurrence of item eg:3
    def index(self, item):
        return self.items.index(item)


    def str (self):
        return str(self.items)

    # using count() to count the occurrences of item eg:3
    def count(self, item):
        return self.items.count(item)

    #  using reverse() to reverse the deque
    def reverse(self):
        self.items.reverse()


if __name__ == '__main__':
    de = deque()
    de.enqueue(1)
    de.enqueue(2)
    de.enqueue(3)
    de.enqueue_front(4)
    de.extend([5, 6, 7])
    de.extendleft([8, 9, 10])
    print(de.dequeue())
    print(de.dequeue_front())
    print(de.remove(2))
    print(de.size())
    print(de.index(1))
    print(de.insert(2, 11))
    print(de.str())
    print(de.count(1))
    de.extend([12, 13, 14])
    de.extendleft([15, 16, 17])
    print(de.str())
    de.reverse()
    print(de.str())
    print(de.isEmpty())
    print(de.size())
    print(de)



    
    