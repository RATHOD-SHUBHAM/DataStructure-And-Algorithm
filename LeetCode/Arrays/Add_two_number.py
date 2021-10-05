class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        current_carry = 0
        head = cur = ListNode(0)

        while p1 or p2 or current_carry:
            current_val = current_carry
            current_val += 0 if p1 is None else p1.val
            current_val += 0 if p2 is None else p2.val
            if current_val >= 10:
                current_val -= 10
                current_carry = 1
            else:
                current_carry = 0

            cur.next = ListNode(current_val)
            cur = cur.next

            if p1 is None and p2 is None:
                break
            elif p1 is None:
                p2 = p2.next
            elif p2 is None:
                p1 = p1.next
            else:
                p1 = p1.next
                p2 = p2.next

        return head.next



def result(l):
    if l is None:
        return ''
    else:
        return str(l.val)+'-->'+result(l.next)


def main():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    print(result(l1))

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    print(result(l2))

    s = Solution()
    l3 = s.addTwoNumbers(l1,l2)
    print(result(l3))




if __name__ == '__main__':
    main()
