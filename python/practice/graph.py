import collections

# Represent Graphs using adjacency lists
class Node(object):
    """ Node to represent each vertex in a graph """
    def __init__(self, name=None, nodes=[]):
        self.name = name
        self.nodes = nodes

class DirectedGraph(object):
    """ Directed graph in the form of a adjacency list """
    def __init__(self):
        # Keys are names of nodes, values are other connections
        self.nodes = collections.defaultdict(list)

if __name__ == '__main__':
    # Create a graph in CTCI pg. 106
    ug = graph.DirectedGraph()

    node_0 = graph.Node(0)
    node_1 = graph.Node(1)
    node_2 = graph.Node(2)
    node_3 = graph.Node(3)

    node_0.nodes = [1]
    node_1.nodes = [2]
    node_2.nodes = [0, 3]
    node_3.nodes = [2]