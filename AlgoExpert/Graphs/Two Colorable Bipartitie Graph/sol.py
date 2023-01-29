# Tc and Sc: O(v + e)

def twoColorable(edges):
    # Let the 2 color be : True and False
    no_of_vertex = len(edges)

    color = [None] * no_of_vertex

    # mark the first node with one color
    color[0] = True

    queue = [0] # first vertex

    while queue:
        vertex = queue.pop(0)

        # BFS
        for child in edges[vertex]:
            # if the child has not been assigned any color yet
            if color[child] ==  None:
                # assign child the opposit color or vertex node
                color[child] = not color[vertex]
                queue.append(child)
            else:
                if color[child] == color[vertex]:
                    return False

    return True