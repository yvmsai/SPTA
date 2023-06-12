
class BellmanFord:
    # Assigning values when initialing the object
    def __init__(self, vertices, edge_weights):
        self.V = vertices  # No. of vertices
        self.graph = edge_weights

    # Adding edges to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # Function to print the values
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    #  Function to find shortest distance from src to
    # destination using Bellman-Ford algorithm.
    def BellmanFord(self, src, dest):

        # Initialize distances from src to all other vertices
        dist = [float("Inf")] * self.V
        dist[src] = 0.0

        # Loop for all edges for vertices -1
        for _ in range(self.V - 1):
            # calculating distance value for adjancent vertices from parent vertex
            for u, v, w in self.graph:
                if dist[u] != dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Check for negative weights in the graph
        for u, v, w in self.graph:
            if dist[u] != dist[u] + w < dist[v]:
                print("BellmanFord contains negative weight cycle")
                return
        return dist
