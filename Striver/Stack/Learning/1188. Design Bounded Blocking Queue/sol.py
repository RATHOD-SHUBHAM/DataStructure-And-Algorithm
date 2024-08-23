from threading import Semaphore
from collections import deque  # Ensure deque is imported

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        # Initialize the queue with given capacity.
        self.semaphore_empty_slots = Semaphore(capacity)  # Semaphore to track empty slots
        self.semaphore_filled_slots = Semaphore(0)        # Semaphore to track filled slots
        self.queue = deque()                               # Use deque for queue operations

    def enqueue(self, element: int) -> None:
        # Add an element to the end of the queue.
        self.semaphore_empty_slots.acquire()  # Decrease the counter of empty slots, wait if no empty slots
        self.queue.append(element)            # Add the element to the queue
        self.semaphore_filled_slots.release() # Increase the counter of filled slots, signaling dequeue if slots are filled

    def dequeue(self) -> int:
        # Remove and return an element from the front of the queue.
        self.semaphore_filled_slots.acquire()  # Decrease the counter of filled slots, wait if no filled slots
        element = self.queue.popleft()         # Remove the element from the queue
        self.semaphore_empty_slots.release()   # Increase the counter of empty slots, signaling enqueue if slots are available
        return element                         # Return the dequeued element

    def size(self) -> int:
        # Get the current number of elements in the queue.
        return len(self.queue)             # Return the size of the queue
