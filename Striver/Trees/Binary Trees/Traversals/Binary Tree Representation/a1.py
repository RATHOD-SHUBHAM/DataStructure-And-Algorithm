# ------------------------- Index -------------------------------------

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



# ------------------------- Child -------------------------------------

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
    n = len(nodes)
    
    # Use a list to hold all the nodes (from the array)
    tree_nodes = [root]
    
    index = 0  # Index to start at the root node
    parent_idx = ((n-1)-1) // 2 # parentIdx of last node = (i-1)/2
    for i in range(1, parent_idx+1):
    # Jump 2 - Since we have 2 children.
    # for i in range(1, n, 2):
        current_node = tree_nodes[index]  # Current node we're assigning children to
        
        # Left child index
        left_index = 2*index + 1
        if left_index < n:  # If within bounds
            left_child = TreeNode(nodes[left_index])
            current_node.left = left_child
            tree_nodes.append(left_child)  # Add left child to the node list
            
        # Right child index
        right_index = 2*index + 2
        if right_index < n:  # If within bounds
            right_child = TreeNode(nodes[right_index])
            current_node.right = right_child
            tree_nodes.append(right_child)  # Add right child to the node list
        
        # Move to the next parent node (in the tree_nodes list)
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
