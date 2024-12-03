class TreeNode:
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

def construct_tree(nodes):
    if not nodes:
        return None

    # Create the root node
    root = TreeNode(nodes[0])
    
    # Queue for level order traversal (holds nodes yet to be fully processed)
    queue = [root]
    
    # Initialize index to process the remaining nodes
    index = 1
    
    # Loop to construct the tree
    while index < len(nodes):
        current_node = queue.pop(0)  # Get the next node to process
        
        # Assign left child
        if index < len(nodes):
            left_child = TreeNode(nodes[index])
            current_node.left = left_child
            queue.append(left_child)  # Add to queue for future processing
            index += 1
        
        # Assign right child
        if index < len(nodes):
            right_child = TreeNode(nodes[index])
            current_node.right = right_child
            queue.append(right_child)  # Add to queue for future processing
            index += 1
    
    return root

# Example usage:
nodes = [1, 2, 3, 4, 5, 6, 7]
root = construct_tree(nodes)

# To verify, you can write a helper function to print level-order traversal (just for testing)
def print_level_order(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

# Print the level-order traversal of the constructed tree
print(print_level_order(root))  # Expected output: [1, 2, 3, 4, 5, 6, 7]
