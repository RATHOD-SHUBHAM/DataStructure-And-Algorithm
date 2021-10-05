"""

380. Insert Delete GetRandom O(1)

Implement the RandomizedSet class:

bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
Follow up: Could you implement the functions of the class with each function works in average O(1) time?



Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.



"""
# If i keep the print statment :  it will say Output Limit Exceeded



class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # you can initialise _dict and _nums are variable name to look fancy . we can just write as dict and nums also
        self._dict = {}
        self._nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

        '''
        1] If val is already present --> return false, we dont want to add anything.
        2] if not
            a] Add val into list
            b] Add val to dict
            c] Return True

        '''
        if val in self._dict:
            return False
        self._nums.append(val)
        self._dict[val] = len(self._nums) - 1  # key value pair starting from 0.

        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

        '''
        1] If value is not present return False
        2] If present: 
            a] check where the val is present in dict and get the value(key:value) from it.
            b] once we get the value from dict we can look that position up list. And the replace value at that position with last value of the list.
            c] Change the (key:value) value in the dict as well. Because we replaced the element in the list.
            d] Pop element from both dict and list
            e] return true

        '''
        if not val in self._dict:
            return False
        # print("the list is : ",self._nums)
        # print("the dict is : ",self._dict)
        idx = self._dict[val]  # get the value from the key
        # print("the idx is : ",idx)

        self._nums[idx] = self._nums[-1]  # replacae value at that position with last element.
        # print("the list is : ",self._nums)

        self._dict[self._nums[-1]] = idx

        # print("the dict is : ",self._dict)

        self._nums.pop()
        # self._dict.pop(val)
        # or
        del self._dict[val]

        # print(self._nums)
        # print(self._dict)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """

        # return self._nums[random.randint(0,len(self._nums) - 1 )]
        # or
        return choice(self._nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()