class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def findPairs(head: Node, k: int) -> [[int]]:

    # code here
    op = []
    
    front = head

    # get to tail
    back = head
    while back.next:
        back = back.next
    
    # print(front.data)
    # print(back.data)
    
    while front.data < back.data:
        cur_sum = front.data + back.data
        
        if cur_sum > k:
            back = back.prev
        elif cur_sum < k:
            front = front.next
        else:
            op.append((front.data, back.data))
            front = front.next
            back = back.prev
    
    return op
