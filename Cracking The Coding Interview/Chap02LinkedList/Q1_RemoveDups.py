from Chap02LinkedList.Linked_List import LinkedList

# Time and Space : O(n)
# logic:
def remove_dup(Linked_List):
    # initalzing node to head
    node = Linked_List.head

    # checking if my linked list has a element or if it is a single elememt
    if node == None or node.next == None:
        return Linked_List

    # create a hash
    hash = set()

    # adding first element to hash
    hash.add(node.value)
    while node.next != None:
        if node.next.value in hash:
            node.next = node.next.next
        else:
            hash.add(node.next.value)
            node = node.next

    return Linked_List



def main():
    # generate 100 duplicate values from 0-9
    Linked_List = LinkedList.generate(100, 0, 9)
    print("The Linked List is: ")
    print(Linked_List)
    print("\n")
    print("The Unique elements are: ")
    print(remove_dup(Linked_List))


if __name__ == '__main__':
    main()
