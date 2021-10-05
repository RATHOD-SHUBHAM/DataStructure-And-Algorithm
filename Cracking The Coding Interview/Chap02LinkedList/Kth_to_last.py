from Chap02LinkedList.Linked_List import LinkedList

#todo:  iterative method
# O(n) and space O(1)
def kth_to_last(LinkList,k):
    # print(len(LinkList))
    #O(1)
    diff = len(LinkList) - k
    # print(diff)

    node = LinkList.head
    for i in range(diff):
        if node.next is not None:
            node = node.next

    while node is not None:
        print(node.value)
        node = node.next

def main():
    LL = LinkedList.generate(15, 1, 9)
    print(LL)
    kth_to_last(LL,3)


if __name__ == '__main__':
    main()
