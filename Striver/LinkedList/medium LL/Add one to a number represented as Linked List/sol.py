# Tc: O(n) | Sc: O(1)

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.
def rev_LL(head_node):
    prev = None
    cur = head_node

    while cur:
        next_node = cur.next

        cur.next = prev
        
        prev = cur
        cur = next_node
    

    return prev


def addOne(head: Node) -> Node:
    dummy = new_LL = Node(-1)
    # Reverse LL
    head_node = rev_LL(head)


    cur_node = head_node
    carry = 1


    while cur_node or carry:
        
        cur_sum = carry

        cur_sum += cur_node.data if cur_node else 0

        
        if cur_sum > 9:
            carry = 1
            cur_sum -= 10
        else:
            carry = 0

        # print("cur_sum : ", cur_sum)
        new_LL.next = Node(cur_sum)
        new_LL = new_LL.next

        if cur_node is not None:
            cur_node = cur_node.next
        else:
            continue
    
    # print(dummy.next)
    new_head = rev_LL(dummy.next)

    return new_head