'''
Always read the input and output format properly

enqueue method has a animal parameter, 
animal[0] represents the number of the animal, 
animal[1] represents the type of the animal, 
    0 for cat and 1 for dog.

dequeue* method returns [animal number, animal type], 
if there's no animal that can be adopted, return [-1, -1].

'''

from collections import deque
from typing import List
class AnimalShelter:
    def __init__(self) -> None:
        self.dog = deque()
        self.cat = deque()

    def enqueue(self,animal: List[int]) -> None:
        if animal[1] == 1:
            self.dog.append(animal[0])
        else:
            self.cat.append(animal[0])

    def dequeueAny(self) -> List[int]:
        if len(self.dog) == 0:
            return self.dequeueCat()
        
        if len(self.cat) == 0:
            return self.dequeueDog()

        if self.dog[-1] < self.cat[-1]:
            return self.dequeueDog()
        else:
            return self.dequeueCat()
        
    def dequeueDog(self) -> List[int]:
        if len(self.dog) == 0:
            return [-1, -1]
        else:
            return [self.dog.popleft(), 1]

    def dequeueCat(self) -> List[int]:
        if len(self.cat) == 0:
            return [-1, -1]
        else:
            return [self.cat.popleft(), 0] 



# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()