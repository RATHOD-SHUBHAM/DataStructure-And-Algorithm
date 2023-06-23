# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        #  it is guaranteed that the given node node is not the last node in the linked list.
        # so we know for sure we will have atleast one node after the curNode
        # So copy the next node information to the curNode and delete the next node
        
        nextNode = node.next
        # copy data from next to curNode
        node.val = nextNode.val
        # change the pointer of next node
        node.next = nextNode.next
        nextNode.next = None
        # del the nextNode
        del(nextNode)