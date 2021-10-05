def deleteNode(Link_List,key):
    node = Link_List.head

    while node is not None and node.value == key:
        node = node.next
        Link_List.head = node

    prevNode = None
    while node is not None:
        while node is not None and node.value != key:
            prevNode = node
            node = node.next

        if node is None:
            return Link_List

        prevNode.next = node.next

        node = node.next

    print("the new linked list")

