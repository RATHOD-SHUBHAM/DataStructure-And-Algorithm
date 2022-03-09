# Time = O(nlogn)
# space = O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        # base case
        if not head or not head.next: 
            return head
        
        # return the length of linked list
        total_length = self.getSize(head)
        # print("total_length : ",total_length)
        
        # initialize pointers
        dummy = ListNode(0)
        dummy.next = head
        start = None
        dummy_start = None
        size =  1
        
        while size < total_length:
            dummy_start = dummy
            start = dummy.next 
            
            while start:
                left = start
                print("left : ",left)
                
                right = self.split(left, size) # start from left, cut with size=size
                print("right : ",right)
                print("\n")
                
                start = self.split(right, size) # start from right, cut with size=size
                print("start : ",start)
                print("\n")
                
                dummy_start = self.merge(left, right, dummy_start)  # returned tail = next dummy_start
                print("dummy start: ",dummy_start)
                print("\n")
            size *= 2
        
        return dummy.next
        
    def getSize(self, head):
        # Simply count the length of linked list
        counter = 0
        while head:
            counter +=1
            head = head.next
        return counter
        
    def split(self, head, size):
        # given the head & size, return the the start node of next chunk
        for i in range(size-1):
            # print("i : ",i)
            if not head: 
                break 
            head = head.next

        if not head: 
            return None
        next_start = head.next 
        head.next = None  #disconnect

        return next_start
        
    def merge(self, l1, l2, dummy_start):
        # Given dummy_start, merge two lists, and return the tail of merged list
        curr = dummy_start
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1 
                l1 = l1.next # this will become None
            else:
                curr.next = l2
                l2 = l2.next # this will become None
            curr = curr.next # this will be the first node

        # first node points to second node
        curr.next = l1 if l1 else l2

        while curr.next: 
            curr = curr.next  # Find tail

        # the returned tail should be the "dummy_start" node of next chunk
        return curr  
        
        
                