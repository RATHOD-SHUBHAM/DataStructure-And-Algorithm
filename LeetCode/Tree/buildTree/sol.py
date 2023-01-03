tree = [None] * 10 # arbitary number

# adding root node
def root(node):
    if tree[0] != None:
        print("root node already exist")
    else:
        tree[0] = node

# adding left child to the parent node
def set_left(left_node, parentIdx):
    if tree[parentIdx] == None:
        print("parent doesnot exist")
    else:
        # (2 * n) + 1
        leftChildIdx = (2 * parentIdx) + 1
        tree[leftChildIdx] = left_node

# adding right child to parent node
def set_right(right_node, parentIdx):
    if tree[parentIdx] == None:
        print("parent doesnot exist")
    else:
        # right child = ( 2 * n ) + 2
        rightChildIdx = (2 * parentIdx) + 2
        tree[rightChildIdx] = right_node

def print_tree():
    n = len(tree)

    for i in range(n):
        if tree[i] == None:
            break
        print(tree[i])






# Driver Code
if __name__ == '__main__':
    root('A')
    set_left('B', 0)
    set_right('C', 0)
    set_left('D', 1)
    set_right('E', 1)
    set_right('F', 2)
    print_tree()