class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def front(self):
        if self.head == None:
            return
        
        ptr = self.head
        self.head = self.head.next
        ptr.next = None
        del(ptr)

    def end(self):
        if self.head == None:
            return
        
        scnd_lst = self.head

        # traverse to second last pointer
        while scnd_lst.next and scnd_lst.next.next:
            scnd_lst = scnd_lst.next
        
        # get the last node
        lst_node = scnd_lst.next

        # make the second last as last
        scnd_lst.next = None

        # delete the last
        del(lst_node)
        
