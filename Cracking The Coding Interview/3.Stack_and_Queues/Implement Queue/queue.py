'''
QUEUE uses FIFO (First In First Out) principle.

Operations:
1. enqueue(x) - add an element x to the end of the queue
2. dequeue() - remove the first element from the queue
3. peek() - return the first element from the queue
4. isEmpty() - return true if the queue is empty
5. size() - return the number of elements in the queue

'''

import queue


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def min(self):
        return min(self.items)

    def max(self):
        return max(self.items)

    def __str__(self):
        return str(self.items)

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.min())
    print(queue.max())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.isEmpty())
    print(queue.size())
    print(queue)
    