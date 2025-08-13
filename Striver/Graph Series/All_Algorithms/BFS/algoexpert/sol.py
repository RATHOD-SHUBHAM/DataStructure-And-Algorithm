# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        root = self

        queue = [root]

        while queue:
            node = queue.pop(0)

            array.append(node.name)

            for child in node.children:
                queue.append(child)

        # print(array)
        return array