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
    
    def del_Key(self, key):
        if self.head == None:
            return
        
        curNode = self.head
        prevNode = None

        while curNode != None:
            if curNode.data == key:

                # check if the head node is a key element
                if curNode == self.head:
                    # move the head to the front
                    self.head = self.head.next
                    curNode = self.head
                else:
                    prev.next = curNode.next
                    curNode = curNode.next
            
            else:
                prev = curNode
                curNode = curNode.next

        return self.head
    

    def del_position(self, position):
        if self.head == None:
            return
        
        curNode = self.head
        prevNode = None
        curPos = 0

        # check if position is a negative value
        if position < curPos:
            print("Posiion is not valid")
            return

        # if postion == 0
        if position == curPos:
            self.head = self.head.next
            return
        
        while curNode != None and curPos < position:
            prevNode = curNode
            curNode = curNode.next
            curPos += 1

        # if the postion is larger than linkedlist
        if curPos < position:
            print("Node not available")
            
        # we are at the position
        elif curPos == position:
            prevNode.next = curNode.next
            del(curNode)
            return

        


        
        

        
        

        
        
