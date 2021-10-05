class Node:
    def __init__(self, root):
        self.left = None
        self.right = None
        self.root = root

    def insert(self, root):
        if self.root:
            if root < self.root:
                if self.left is None:
                    self.left = Node(root)
                else:
                    self.left.insert(root)
            elif root > self.root:
                if self.right is None:
                    self.right = Node(root)
                else:
                    self.right.insert(root)
            else:
                self.root = root

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.root)
        if self.right:
            self.right.printTree()


def main():
    root = Node(3)
    root.insert(9)
    root.insert(20)
    root.insert(15)
    root.insert(7)
    root.printTree()


if __name__ == '__main__':
    main()
