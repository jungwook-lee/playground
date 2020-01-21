class Node(object):
    def __init__(self, val = 0, neighbors=None):
        # Note value is int
        self.val = val
        # Note is a [<Node>]
        if neighbors is None:
            self.neighbors = []
        else:
            self.neighbors = neighbors

    def __repr__(self):
        return '<Node {}>'.format(self.val)

def cloneGraph(node):
    mem = dict()
    def clone_helper(node):
        if node.val in mem:
            print("{} is already added skip!".format(node.val))
            return mem[node.val]
        # clone the current node
        print("Adding new node {}".format(node.val))
        new_node = Node(val=node.val)
        mem[node.val] = new_node
        # clone recursively
        for neighbor in node.neighbors:
            new_neigh = clone_helper(neighbor)
            print("Adding new neighbor {} to {}".format( \
                            new_neigh.val, new_node.val))
            print("{}".format(new_node.val), new_node.neighbors)
            new_node.neighbors.append(new_neigh)
        return new_node
    return clone_helper(node)

if __name__ == '__main__':
    # construct a graph
    node_1 = Node(val=1)
    node_2 = Node(val=2)
    node_3 = Node(val=3)
    node_4 = Node(val=4)
    node_1.neighbors = [node_2, node_4]
    node_2.neighbors = [node_1, node_3]
    node_3.neighbors = [node_2, node_4]
    node_4.neighbors = [node_1, node_3]

    out = cloneGraph(node_1)
    print(id(out))
    print(out.val, out.neighbors, id(out.neighbors))
    out = out.neighbors[0]
    print(id(out))
    print(out.val, out.neighbors, id(out.neighbors))
