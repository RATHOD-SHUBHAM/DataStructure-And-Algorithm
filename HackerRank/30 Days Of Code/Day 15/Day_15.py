class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        # Complete this method
        # if my linked list doesnot have any elements then create a node and make it as head
        if head is None:
            head = Node(data)
            self.tail = head
        # create a new node, make my prev node point to the new node and make my new node as tail
        else:
            node = Node(data)
            self.tail.next = node
            self.tail = node
        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head);