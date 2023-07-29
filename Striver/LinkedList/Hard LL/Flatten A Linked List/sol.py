class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child


# Merge Sort in Linked List
def mergeLinkedList(L1, L2):
    if not L1:
        return L2
    
    if not L2:
        return L1
    
    merged_LL = None

    if L1.data < L2.data:
        merged_LL = L1
        L1.child = mergeLinkedList(L1.child, L2)
    else:
        merged_LL = L2
        L2.child = mergeLinkedList(L1, L2.child)
    
    merged_LL.next = None
    return merged_LL

# Merge Sort + Recursion 
def flattenLinkedList(head: Node) -> Node:
    # Write your code here
    if not head or not head.next:
        return head

    curNode = head

    # recursive call to reach the end of the Linked List
    curNode.next = flattenLinkedList(curNode.next)

    # Merge the Linked List
    curNode = mergeLinkedList(curNode, curNode.next)

    return curNode