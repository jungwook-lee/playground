""" Practice Implementing Graph Algorithms """
import queue
import graph
import collections


def depth_first_search(node, visited=collections.defaultdict(bool)):
    """ Mimics a search dfs algorithm by printing the values """
    if node is None:
        return
    print(node.name)
    visited[node.name] = True
    for n in node.nodes:
        if not visited[n.name]:
            depth_first_search(n, visited)

def breadth_first_search(node):
    """ Mimics a bfs search by printing the values """
    if node is None:
        return
    visited = collections.defaultdict(bool)
    Q = queue.Queue(0)
    Q.put(node)
    visited[node.name] = True

    while (not Q.empty()):
        # deque first item
        cur_node = Q.get()
        print(cur_node.name)
        for n in cur_node.nodes:
            if not visited[n.name]:
                visited[n.name] = True
                Q.put(n)


if __name__ == '__main__':
    # Create a graph in CTCI pg. 107
    ug = graph.DirectedGraph()

    node_0 = graph.Node(0)
    node_1 = graph.Node(1)
    node_2 = graph.Node(2)
    node_3 = graph.Node(3)
    node_4 = graph.Node(4)
    node_5 = graph.Node(5)

    node_0.nodes = [node_1, node_4, node_5]
    node_1.nodes = [node_3, node_4]
    node_2.nodes = [node_1]
    node_3.nodes = [node_2, node_4]

    print('DFS order:')
    depth_first_search(node_0)
    print('BFS order:')
    breadth_first_search(node_0)