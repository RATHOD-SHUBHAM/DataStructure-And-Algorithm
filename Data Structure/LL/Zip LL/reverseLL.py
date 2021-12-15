'''
reverse 
   5 -> 6
to 
   6 -> 5

'''

def reversedLL(self, head):
    prev = None
    curNode = head

    while curNode:
        nextNode = curNode.next
        curNode.next = prev
        prev =  curNode
        curNode = nextNode
    return prev