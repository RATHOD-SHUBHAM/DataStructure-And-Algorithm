'''
A node can be added in three ways 
    1) At the front of the linked list 
    2) After a given node. 
    3) At the end of the linked list.

'''

# 1. Following are the 4 steps to add a node at the front.
def push(self,new_val):
    new_node = Node(new_val)
    if self.head is None:
        self.head = new_node
        return
        
    new_node.next = self.head
    self.head = new_node

# 2. Add a node after a given node: (5 steps process) 
def insert_after(self,prev_node,new_val):
    new_node = Node(new_val)

    if prev_node is None:
        return

    new_node.next = prev_node.next

    prev_node.next = new_node

# 3. Add a node at the end: (6 steps process) 

def end(self,new_val):
    new_node = Node(new_val)
    if self.head is None:
        self.head = new_node
        return

    last = self.head
    while last.next:
        last = last.next

    last.next = new_node
    