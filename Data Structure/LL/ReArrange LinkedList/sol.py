# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def rearrangeLinkedList(head, k):
    # Write your code here.
    smallHead = None
    smallTail = None
    equalHead = None
    equalTail = None
    largeHead = None
    largeTail = None
	
    curNode = head

    while curNode:
        if curNode.value < k:
            smallHead, smallTail = createLL(smallHead,smallTail,curNode)
        elif curNode.value > k:
            largeHead,largeTail = createLL(largeHead, largeTail, curNode)
        else:
            equalHead, equalTail = createLL(equalHead, equalTail, curNode)
            
        prevNode = curNode
        curNode = curNode.next
        prevNode.next = None
        
    firstHead, firstTail = connectLL(smallHead, smallTail, equalHead, equalTail)
    finalHead, _ = connectLL(firstHead, firstTail, largeHead, largeTail)

    return finalHead

def createLL(head,tail,node):
	newHead = head
	newTail = node
	
	if head is None:
		newHead = node
	if tail is not None:
		tail.next = newTail
		
	return(newHead, newTail)

def connectLL(headOne,tailOne,headTwo,tailTwo):
	newHead = headTwo if headOne is None else headOne
	newTail = tailOne if tailTwo is None else tailTwo
	
	if tailOne is not None:
		tailOne.next = headTwo
		
	return(newHead,newTail)