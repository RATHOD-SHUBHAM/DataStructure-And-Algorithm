class Node:
    def __init__(self, val):
        self.val = val
        self.head = None
        self.tail = None

class DLL:
    def __init__(self):
        self.head = None

    def removeHead(self, node):

        if self.head == None or node == None:
            return

        # if node to be deleted is head
        ptr = self.head
        if node == self.head:
            self.head = self.head.next
            ptr.next = None
            del(ptr)
            return
    
    def removeNode(self, node):
        
        if self.head == None or node == None:
            return
        
        # if node to be delted is somewhere in btn
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        node.prev = None
        node.next = None

    def removeTail(self, node):

        if self.head == None or node == None:
            return
        
        # Remove last node
        lastNode = self.head

        while lastNode.next:
            lastNode = lastNode.next

        lastNode.prev.next = lastNode.next
        lastNode.prev = None
        lastNode.next = None
        del(lastNode)

    def removeNodewithVal(self, val):

        if self.head == None:
            return

        ptr = self.head
        dup = None # dupliicate pointer

        while ptr:
            if ptr.val == val:
                if ptr == self.head:
                    self.head = self.head.next
                    ptr.next = None
                    ptr.prev = None
                    ptr = self.head
                else:
                    dup = ptr
                    ptr = ptr.next

                    dup.prev.next = dup.next
                    dup.prev = None
                    dup.next = None
                    del(dep)
                    
            else:
                ptr = ptr.next


        

        
