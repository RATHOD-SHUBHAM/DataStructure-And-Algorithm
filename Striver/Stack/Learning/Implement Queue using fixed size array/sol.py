class SillyQueue:
    
    def __init__(self):
        self.MAX = 5
        # Main Array
        self.head = [None] * self.MAX
        self.tail = self.head
        self.headPtr = 0
        self.tailPtr = 0
    
    def enqueue(self, x):
        if self.tailPtr == self.MAX - 1:
            # create a new array and link it 
            new_array = [None] * self.MAX
            # Attach new array to main array
            self.tail[self.MAX - 1] = new_array
            # Tail will now point to new array
            self.tail = new_array
            self.tailPtr = 0
        self.tail[self.tailPtr] = x
        self.tailPtr += 1
    
    def dequeue(self):
        if self.headPtr == self.MAX - 1:
            # Move the main array to the new array
            self.head = self.head[self.MAX - 1]
            self.headPtr = 0
        value = self.head[self.headPtr]
        self.headPtr += 1
        return value


